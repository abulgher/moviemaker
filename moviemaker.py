# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:55:38 2022

@author: elog-admin
"""

from PyQt5.QtWidgets import  QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore
Signal = QtCore.pyqtSignal
Slot = QtCore.pyqtSlot
from moviemaker_ui import Ui_MainWindow
import logging
import ctypes
import sys
from pathlib import Path
from PIL import Image
import moviepy.video.io.ImageSequenceClip
import moviepy.video.VideoClip
import moviepy.video.io.VideoFileClip
import moviepy.video.compositing.concatenate
import shutil
import time
import random
from proglog import TqdmProgressBarLogger

log = logging.getLogger(__name__)

LEVELS = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
          logging.CRITICAL)

class Signaller(QtCore.QObject):
    signal = Signal(str, logging.LogRecord)
    
class PrologSignaller(QtCore.QObject):
    signal_max = Signal(int)
    signal_progress = Signal(int)
    
class QtHandler(logging.Handler):
    
    def __init__(self, slotfunc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signaller = Signaller()
        self.signaller.signal.connect(slotfunc)
        
    def emit(self, record):
        s = self.format(record)
        self.signaller.signal.emit(s, record)
        
class MyBarLogger(TqdmProgressBarLogger):
    
    def __init__(self, slotfunc_max, slotfunc_progress, *args, **kawrgs):
        super().__init__(*args, **kawrgs)
        self.signaller = PrologSignaller()
        self.signaller.signal_max.connect(slotfunc_max)
        self.signaller.signal_progress.connect(slotfunc_progress)
        
    def emit_max(self, maxi):
        self.signaller.signal_max.emit(maxi)
        
    def emit_progress(self, prog):
        self.signaller.signal_progress.emit(prog)
    
    def bars_callback(self, bar, attr, value, old_value):
        if bar == 't':
            if attr == 'index':
                self.emit_progress(value)
            elif attr == 'total':
                self.emit_max(value)
            else:
                print('{} is {}'.format(attr, value))
        

def ctname():
    return QtCore.QThread.currentThread().objectName()


class Worker(QtCore.QObject):
    
    
    # signal to confirm that the worker did its job
    work_done = Signal(bool, name='work_done')
    # signal to indicate the whole amount of work to do
    how_much_work = Signal(int, name='how_much_work')
    # signal to show how much work has been already done.
    work_progress = Signal(int, name='work_progress')
    
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent=parent)
    
    def get_imagelist(self, input_path, file_filter, display = False, as_path=True):
        extra = {'qThreadName': ctname()}
        if as_path:
            image_list = sorted( [img for img in Path(input_path).glob(file_filter)])
        else:
            image_list = sorted( [str(img) for img in Path(input_path).glob(file_filter)])
        if display:
            log.info('Found a total of {} images in the input folder matchign the filter'.format(len(image_list)),extra=extra)
            for img in image_list:
                log.info(img.name, extra=extra)
        return image_list

class StupidWorker(Worker):
    @Slot()
    def start(self):
        extra = {'qThreadName': ctname() }
        log.debug('Started work', extra=extra)
        i = 1
        # Let the thread run until interrupted. This allows reasonably clean
        # thread termination.
        while not QtCore.QThread.currentThread().isInterruptionRequested():
            delay = 0.5 + random.random() * 2
            time.sleep(delay)
            level = random.choice(LEVELS)
            log.log(level, 'Message after delay of %3.1f: %d', delay, i, extra=extra)
            i += 1


class ConverterWorker(Worker):


    def update_parameters(self, input_path, file_filter, output_path, output_format):
        self.converter_input_folder = Path(input_path)
        self.converter_output_folder = Path(output_path)
        self.converter_filter = file_filter
        self.converter_output_format = output_format
    
    
    @Slot()
    def start(self):
        
        start_time = time.time()
        self.extra = {'qThreadName': ctname()}
        log.debug('Started work {}'.format(self.objectName()), extra=self.extra)
        log.debug('Input path: {}'.format(str(self.converter_input_folder)), extra=self.extra)
        log.debug('File filter: {}'.format(self.converter_filter), extra=self.extra)
        log.debug('Output path: {}'.format(str(self.converter_output_folder)), extra=self.extra)
        log.debug('Output format: {}'.format(self.converter_output_format), extra=self.extra)
        
        # make the dest folder
        self.converter_output_folder.mkdir(exist_ok=True)

        # get the list of images
        self.converter_image_list = self.get_imagelist(Path(self.converter_input_folder), self.converter_filter) 
        
        # reset progress bar and set its max
        self.how_much_work.emit(len(self.converter_image_list))
        self.work_progress.emit(0)
        i = 1
        
        # start the real work
        for img in self.converter_image_list:
            
             # stop the loop here if asked to sktop
            if QtCore.QThread.currentThread().isInterruptionRequested():
                log.info('Received interruption request', extra=self.extra)
                break            
            outputfilename = Path(str(img.stem)+'.'+self.converter_output_format)
            try:
                log.info('Converting {} in {}'.format(str(img.name), self.converter_output_format), extra=self.extra)
                im = Image.open(img)
                im = im.convert('RGB')
                im.save(self.converter_output_folder / outputfilename, self.converter_output_format)
            except Exception as e:
                log.exception(e, extra=self.extra)
            self.work_progress.emit(i)
            i += 1
        self.work_done.emit(True)
        delta_time = time.time() - start_time
        log.info('Conversion of {} images finished in {:.3f} seconds'.format(len(self.converter_image_list), delta_time), extra=self.extra)
        
class SequenceWorker(Worker):
    
    def update_parameters(self, input_path, file_filter, output_file, fps):
        self.sequence_input_folder = Path(input_path)
        self.sequence_file_filter = file_filter
        self.sequence_output_file = Path(output_file)
        self.sequence_fps = fps
        
    @Slot()
    def start(self):
        start_time = time.time()
        self.extra = {'qThreadName': ctname()}
        
        self.how_much_work.emit(1)
        self.work_progress.emit(0)
        
        # moviepy requires a proglog progress bar handler.
        self.sequence_proglog_bar = MyBarLogger(self.how_much_work.emit, self.work_progress.emit, bars=('t',))
        
        
        #make sure that the directory of the outputfile exists
        self.sequence_output_file.parent.mkdir(exist_ok=True)
        log.info('Generating image sequence', extra=self.extra)
        log.info('It may take several minutes', extra=self.extra)
        image_list = self.get_imagelist(self.sequence_input_folder, self.sequence_file_filter, display=False, as_path=False)
        try:
            clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_list, fps=self.sequence_fps)
            self.work_progress.emit(1)        
            log.info('Generating output file {}'.format(self.sequence_output_file.name),extra=self.extra)
            log.info('It may take several minutes', extra=self.extra)
            clip.write_videofile(filename=str(self.sequence_output_file), logger=self.sequence_proglog_bar)
            log.info('Writing output file {} on disk'.format(self.sequence_output_file.name),extra=self.extra)
        except Exception as e:
            log.exception(e,extra=self.extra)
        self.work_done.emit(True)
        delta_time = time.time() - start_time
        log.info('Generation of video clip finished {:.3f} seconds'.format(delta_time), extra=self.extra)        
       
       
class JoinWorker(Worker):
    
    def update_parameters(self, input_file1, input_file2, output_file):
        self.input_file1 = Path(input_file1)
        self.input_file2 = Path(input_file2)
        self.output_file = Path(output_file)
        
    @Slot()
    def start(self):
        start_time = time.time()
        self.extra = {'qThreadName': ctname()}
        
        # moviepy requires a proglog progress bar handler.
        self.join_proglog_bar = MyBarLogger(self.how_much_work.emit, self.work_progress.emit, bars=('t',))
        
        self.how_much_work.emit(3)
        self.work_progress.emit(0)
        try:
            log.info('Loading video {}'.format(self.input_file1.name), extra=self.extra)
            clip1 = moviepy.video.io.VideoFileClip.VideoFileClip(str(self.input_file1))
            self.work_progress.emit(1)
            
            log.info('Loading video {}'.format(self.input_file2.name), extra=self.extra)
            clip2 = moviepy.video.io.VideoFileClip.VideoFileClip(str(self.input_file2))
            self.work_progress.emit(2)
            log.info('Concatenating the input videos', extra=self.extra)
            outclip = moviepy.video.compositing.concatenate.concatenate_videoclips([clip1, clip2])
            self.work_progress.emit(3)
            
            self.work_progress.emit(0)
            log.info('Writing the output file {}'.format(self.output_file.name), extra=self.extra)
            outclip.write_videofile(str(self.output_file), logger=self.join_proglog_bar)
        except Exception as e:
            log.exception(e, extra=self.extra)
        self.work_done.emit(True)
        delta_time = time.time() - start_time
        log.info('Joining of video clips finished {:.3f} seconds'.format(delta_time), extra=self.extra)   
        
class MovieMakerWindow(QMainWindow, Ui_MainWindow):
    
    COLORS = {
        logging.DEBUG: 'black',
        logging.INFO: 'blue',
        logging.WARNING: 'orange',
        logging.ERROR: 'red',
        logging.CRITICAL: 'purple'        
        }
       
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)

        # create a logging handler with a slot function pointing to update_status
        self.handler = QtHandler(self.update_status)
        self.extra = {'qThreadName': ctname()}
        

        
        # create a formatter and assign it to the handler
        fs = '[%(asctime)s] %(qThreadName)-12s %(levelname)s: %(message)s'
        formatter = logging.Formatter(fs, datefmt='%Y%m%d-%H:%M:%S')
        self.handler.setFormatter(formatter)
        log.addHandler(self.handler)
        
        self.workers = {}
        self.worker_threads = {}
        
        
        self.start_thread()
        
        self.converter_start_button.clicked.connect(self.workers['Converter'].start)
        self.converter_start_button.clicked.connect(lambda: self.enable_inputs(False))
        self.sequence_start_button.clicked.connect(self.workers['Sequence'].start)
        self.sequence_start_button.clicked.connect(lambda: self.enable_inputs(False))
        self.join_start_button.clicked.connect(self.workers['Join'].start)
        self.join_start_button.clicked.connect(lambda: self.enable_inputs(False))
        
        
        self.connectSignalsSlot()
        
        
    def start_thread(self):
        
        worker_list = {
            'Converter' : {
                'WorkerClassType' : 'ConverterWorker',
                'WorkerObjectName': 'Converter',
                'WorkerThreadName': 'ConverterThread'                
                },
            'Sequence' : {
                'WorkerClassType' : 'SequenceWorker',
                'WorkerObjectName': 'Sequence',
                'WorkerThreadName': 'SequenceThread'                
                },
            'Join' : {
                'WorkerClassType' : 'JoinWorker',
                'WorkerObjectName': 'Join',
                'WorkerThreadName': 'JoinThread'                
                }   
            }
        
        for key,worker in worker_list.items() :
            new_worker = globals()[worker['WorkerClassType']]()
            new_worker.parent = self
            new_worker_thread = QtCore.QThread()
            new_worker.setObjectName(worker['WorkerObjectName'])
            new_worker_thread.setObjectName(worker['WorkerThreadName'])
            new_worker.moveToThread(new_worker_thread)
            new_worker_thread.start()
            new_worker.work_done.connect(self.enable_inputs)
            new_worker.how_much_work.connect(self.progressBar.setMaximum)
            new_worker.work_progress.connect(self.progressBar.setValue)
            self.workers[key] = new_worker
            self.worker_threads[worker['WorkerThreadName']] = new_worker_thread
        
        

    def kill_thread(self):
        for key, thread in self.worker_threads.items():
            if thread.isRunning():
                thread.quit()
                thread.wait()
            else:
                log.debug('Thread {} was dead already'.format(thread.objectName()), extra=self.extra)
                
    def force_quit(self):
        # TODO: don't like this implementation
        for key, thread in self.worker_threads.items():
            if thread.isRunning():
                thread.quit()
                thread.wait()

                
    @Slot(str, logging.LogRecord)
    def update_status(self, status, record):
        color = self.COLORS.get(record.levelno, 'black')
        s = '<pre><font color="%s">%s</font></pre>' % (color, status)
        self.messagewindow.appendHtml(s)
        
    def connectSignalsSlot(self):   
        self.app.aboutToQuit.connect(self.force_quit)
        self.converter_start_button.clicked.connect(self.enable_inputs)
    

    
    def converter_open_input_folder(self):
        directory = self.converter_input_path_text.text()
        if not directory:
            directory = '.'
        returnpath = QFileDialog.getExistingDirectory(self, 'Input images folder', directory=directory)
        if returnpath:
            self.converter_input_path_text.setText(returnpath)
            self.converter_validate_start()
            
    def converter_open_output_folder(self):
        directory = self.converter_output_path_text.text()
        if not directory:
            directory = '.'
        returnpath = QFileDialog.getExistingDirectory(self, 'Output folder', directory=directory)
        if returnpath:
             self.converter_output_path_text.setText(returnpath)
             self.converter_validate_start()   

    def converter_test_filter(self):
        self.sequence_get_imagelist(Path(self.converter_input_path_text.text()),
                                         self.converter_file_filter_text.text(),
                                         display = True)
            
            
    def converter_validate_start(self):
        
        ok_to_start = True
        ok_to_test = True
        if not self.converter_input_path_text.text():
            ok_to_start = ok_to_start and False     
            ok_to_test = ok_to_test and False
        if not self.converter_file_filter_text.text():
            ok_to_start = ok_to_start and False
            ok_to_test = ok_to_test and False
        if not self.converter_output_path_text.text():
            ok_to_start = ok_to_start and False
        self.converter_start_button.setEnabled( ok_to_start )
        self.converter_test_filter_button.setEnabled( ok_to_test )
        if ok_to_start:
            self.sequence_image_path_text.setText(self.converter_input_path_text.text())
            self.sequence_image_filter_text.setText('*.{}'.format(self.converter_output_format_combobox.currentText().lower()))
            log.debug('Updating converter parameters', extra=self.extra)
            self.workers['Converter'].update_parameters(Path(self.converter_input_path_text.text()), 
                                                    self.converter_file_filter_text.text(),
                                                    Path(self.converter_output_path_text.text()),
                                                    self.converter_output_format_combobox.currentText())
        log.debug('Ready to start the image conversion', extra=self.extra)
    

    def show(self) :
        log.info('Welcome to the Moviemaker GUI.',extra=self.extra)        
        super().show()
    
    def sequence_test_filter(self):
        self.sequence_get_imagelist(Path(self.sequence_image_path_text.text()),
                                    self.sequence_image_filter_text.text(), 
                                    display=True)
    
    def sequence_open_input_folder(self):
        directory = self.sequence_image_path_text.text()
        if not directory:
            directory = '.'
        returnpath = QFileDialog.getExistingDirectory(self, 'Image list folder', directory=directory)
        if returnpath:
            self.sequence_image_path_text.setText(returnpath)
            self.sequence_validate_start()
        
    def sequence_validate_start(self):
        
        ok_to_start = True
        ok_to_test = True
        if not self.sequence_image_path_text.text():
            ok_to_start = ok_to_start and False            
            ok_to_test = ok_to_test and False
        if not self.sequence_image_filter_text.text():
            ok_to_start = ok_to_start and False
            ok_to_test = ok_to_test and False
        if not self.sequence_output_filename_text.text():
            ok_to_start = ok_to_start and False
        if self.sequence_output_filename_text.text() and not self.sequence_output_filename_text.text().endswith('.mp4'):
            ok_to_start = ok_to_start and False
            log.warning('Please select a mp4 output file',extra=self.extra)
        self.sequence_start_button.setEnabled( ok_to_start )
        self.sequence_test_filter_button.setEnabled( ok_to_test )
        

        if ok_to_start :
            log.debug('Updating sequence parameters', extra=self.extra)
            self.workers['Sequence'].update_parameters(Path(self.sequence_image_path_text.text()),
                                                      self.sequence_image_filter_text.text(),
                                                      Path(self.sequence_output_filename_text.text()),
                                                      self.sequence_fpb_spin.value())

    
    
    def sequence_open_output_file(self):
        directory = self.sequence_output_filename_text.text()
        if not directory:
            directory = '.'
        returnpath = QFileDialog.getSaveFileName(self, 'Output filename for the sequence video',
                                                      filter='Videos (*.mp4)',
                                                      directory=directory)
        if returnpath:
            self.sequence_output_filename_text.setText(returnpath[0])
            self.sequence_validate_start()
            
    
    def sequence_open_temp_folder(self):
        returnpath = QFileDialog.getExistingDirectory(self, 'Temporary image folder')
        if returnpath:
            self.sequence_temporary_folder_text.setText(returnpath)
            self.sequence_validate_start()
    
    def sequence_get_imagelist(self, folder, filefilter, display = False):
        image_list = sorted([img for img in folder.glob(filefilter)])
        if display:
            log.info('Found a total of {} images in the input folder matching the filter'.format(len(image_list)),extra=self.extra)
            for img in image_list:
                log.info(img.name,extra=self.extra)
        return image_list
    
    # def sequence_start(self):
        
        
    #     self.sequence_thread = threading.Thread(target=self.sequence_start_thread)
    #     self.sequence_thread.start()
        
    def enable_inputs(self, status=True):
        self.tab_moviemaker.setEnabled(status)
    
    def sequence_start_thread(self):
        self.enable_inputs(False)
        self.sequence_input_folder = Path(self.sequence_image_path_text.text())
        self.sequence_filter = self.sequence_image_filter_text.text()
        self.sequence_output_filename = Path(self.sequence_output_filename_text.text())
        self.sequence_temp_folder = Path(self.sequence_temporary_folder_text.text())
        self.sequence_fps = self.sequence_fpb_spin.value()
        self.sequence_preserve_temp = self.sequence_preserve_tempfiles_checkbok.checkState()
        
        # make the tmp folder and don't complain if it exists already
        self.sequence_temp_folder.mkdir(exist_ok=True)
        
        # get the image list
        self.sequence_image_list = self.sequence_get_imagelist(self.sequence_input_folder,self.sequence_filter, display=False)
        
        
        # convert in png if needed, otherwise just copy to the tmp folder
        for img in self.sequence_image_list:
            
            if img.suffix != '.png':
                outputfile = Path(str(img.stem) + '.png')
                try:
                    log.info('Converting image {} in png'.format(str(img.name)),extra=self.extra)
                    im = Image.open(img)
                    im = im.convert('RGB')
                    im.save( self.sequence_temp_folder / outputfile, 'PNG')
                except Exception as e:
                    log.exception(e,extra=self.extra)
            else:
                log.info("Copying image {} in temporary folder".format(str(img.name)),extra=self.extra)
                dest = self.sequence_temp_folder / img.name
                shutil.copy(img, dest)

        try:                    
            clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(str(self.sequence_temp_folder), fps=self.sequence_fps)
        except Exception as e:
            log.exception(e, extra=self.extra)
        try:
            bar = MyBarLogger()
            log.info('Writing output file {}'.format(self.sequence_output_filename.name),extra=self.extra)
            clip.write_videofile(filename=str(self.sequence_output_filename), logger=bar)
        except Exception as e:
            log.exception(e,extra=self.extra)
            
        if not self.sequence_preserve_temp :
            log.info('Removing temporary folder',extra=self.extra)
            shutil.rmtree(str(self.sequence_temp_folder))
            
        self.enable_inputs(True)
        
    
    def join_start(self):
        pass
    
    def join_validate_start(self):
        ok_to_start = True
        if not self.join_video1_path_text.text():
            ok_to_start = ok_to_start and False
        if not self.join_video2_path_text.text():
            ok_to_start = ok_to_start and False
        if not self.join_outputvideo_path_text.text():
            ok_to_start = ok_to_start and False
        if self.join_outputvideo_path_text.text() and not self.join_outputvideo_path_text.text().endswith('.mp4'):
            ok_to_start = ok_to_start and False
            log.warning('The output file must be an mp4 file', extra=self.extra)
        self.join_start_button.setEnabled( ok_to_start )
        
        if ok_to_start:
            log.debug('Updating joining parameters', extra=self.extra)
            self.workers['Join'].update_parameters(Path(self.join_video1_path_text.text()),
                                                   Path(self.join_video2_path_text.text()),
                                                   Path(self.join_outputvideo_path_text.text()))
        
    
    def join_open_video1(self):
        directory = self.join_video1_path_text.text()
        if not directory:
            directory = '.'
        returnpath = QFileDialog.getOpenFileName(self, 'Select first video to join', filter='Video (*.mp4)', directory=directory)
    
        if returnpath:
            self.join_video1_path_text.setText(returnpath[0])
            self.join_validate_start()
    
    def join_open_video2(self):
        directory = self.join_video2_path_text.text()
        if not directory:
            directory = '.'
        returnpath = QFileDialog.getOpenFileName(self, 'Select second video to join', filter='Video (*.mp4)', directory=directory)
        if returnpath:
            self.join_video2_path_text.setText(returnpath[0])
            self.join_validate_start()
    
    def join_open_output_video(self):
        directory = self.join_outputvideo_path_text.text()
        if not directory:
            directory = '.'
        returnpath = QFileDialog.getSaveFileName(self, 'Select the output file name', filter='Video (*.mp4)', directory=directory)
        if returnpath:
            self.join_outputvideo_path_text.setText(returnpath[0])
            self.join_validate_start()
        
    
def main():
    # to set the icon on the window task bar
    myappid = u'ecjrc.moviemaker.gui.v1.0.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    
    # give a name at the main thread
    QtCore.QThread.currentThread().setObjectName('MovieMaker')   
    
    # set the log level
    logging.getLogger().setLevel(logging.INFO)
    
    # start the Qt App
    app = QApplication(sys.argv)
    win = MovieMakerWindow(app)

    # show the main window 
    win.show()
    
    # execute the main window and eventually exit when done!
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    
    

    

    

    
    
    
    