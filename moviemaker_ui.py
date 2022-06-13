# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/moviemaker_mw.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 613)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icons8-bobina-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tab_moviemaker = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_moviemaker.setToolTip("")
        self.tab_moviemaker.setObjectName("tab_moviemaker")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)
        self.converter_input_path_text = QtWidgets.QLineEdit(self.tab)
        self.converter_input_path_text.setMinimumSize(QtCore.QSize(300, 0))
        self.converter_input_path_text.setObjectName("converter_input_path_text")
        self.gridLayout_4.addWidget(self.converter_input_path_text, 0, 1, 1, 1)
        self.converter_input_path_button = QtWidgets.QToolButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/icons8-opened-folder-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.converter_input_path_button.setIcon(icon1)
        self.converter_input_path_button.setObjectName("converter_input_path_button")
        self.gridLayout_4.addWidget(self.converter_input_path_button, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.converter_file_filter_text = QtWidgets.QLineEdit(self.tab)
        self.converter_file_filter_text.setMinimumSize(QtCore.QSize(300, 0))
        self.converter_file_filter_text.setObjectName("converter_file_filter_text")
        self.gridLayout_4.addWidget(self.converter_file_filter_text, 1, 1, 1, 1)
        self.converter_test_filter_button = QtWidgets.QToolButton(self.tab)
        self.converter_test_filter_button.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/icons8-ok-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.converter_test_filter_button.setIcon(icon2)
        self.converter_test_filter_button.setObjectName("converter_test_filter_button")
        self.gridLayout_4.addWidget(self.converter_test_filter_button, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)
        self.converter_output_format_combobox = QtWidgets.QComboBox(self.tab)
        self.converter_output_format_combobox.setMinimumSize(QtCore.QSize(300, 0))
        self.converter_output_format_combobox.setObjectName("converter_output_format_combobox")
        self.converter_output_format_combobox.addItem("")
        self.converter_output_format_combobox.addItem("")
        self.gridLayout_4.addWidget(self.converter_output_format_combobox, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 3, 0, 1, 1)
        self.converter_output_path_text = QtWidgets.QLineEdit(self.tab)
        self.converter_output_path_text.setMinimumSize(QtCore.QSize(300, 0))
        self.converter_output_path_text.setObjectName("converter_output_path_text")
        self.gridLayout_4.addWidget(self.converter_output_path_text, 3, 1, 1, 1)
        self.converter_output_path_button = QtWidgets.QToolButton(self.tab)
        self.converter_output_path_button.setIcon(icon1)
        self.converter_output_path_button.setObjectName("converter_output_path_button")
        self.gridLayout_4.addWidget(self.converter_output_path_button, 3, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_4)
        self.converter_start_button = QtWidgets.QPushButton(self.tab)
        self.converter_start_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.converter_start_button.sizePolicy().hasHeightForWidth())
        self.converter_start_button.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/icons8-start-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.converter_start_button.setIcon(icon3)
        self.converter_start_button.setObjectName("converter_start_button")
        self.verticalLayout_9.addWidget(self.converter_start_button)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.tab_moviemaker.addTab(self.tab, "")
        self.tab_imagesequence = QtWidgets.QWidget()
        self.tab_imagesequence.setObjectName("tab_imagesequence")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_imagesequence)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab_imagesequence)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.sequence_image_path_text = QtWidgets.QLineEdit(self.tab_imagesequence)
        self.sequence_image_path_text.setMinimumSize(QtCore.QSize(300, 0))
        self.sequence_image_path_text.setObjectName("sequence_image_path_text")
        self.gridLayout_2.addWidget(self.sequence_image_path_text, 0, 1, 1, 1)
        self.sequence_input_open_folder_button = QtWidgets.QToolButton(self.tab_imagesequence)
        self.sequence_input_open_folder_button.setIcon(icon1)
        self.sequence_input_open_folder_button.setObjectName("sequence_input_open_folder_button")
        self.gridLayout_2.addWidget(self.sequence_input_open_folder_button, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_imagesequence)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.sequence_image_filter_text = QtWidgets.QLineEdit(self.tab_imagesequence)
        self.sequence_image_filter_text.setMinimumSize(QtCore.QSize(0, 0))
        self.sequence_image_filter_text.setObjectName("sequence_image_filter_text")
        self.gridLayout_2.addWidget(self.sequence_image_filter_text, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_imagesequence)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.sequence_output_filename_text = QtWidgets.QLineEdit(self.tab_imagesequence)
        self.sequence_output_filename_text.setMinimumSize(QtCore.QSize(0, 0))
        self.sequence_output_filename_text.setObjectName("sequence_output_filename_text")
        self.gridLayout_2.addWidget(self.sequence_output_filename_text, 2, 1, 1, 1)
        self.sequence_output_filename_button = QtWidgets.QToolButton(self.tab_imagesequence)
        self.sequence_output_filename_button.setIcon(icon1)
        self.sequence_output_filename_button.setObjectName("sequence_output_filename_button")
        self.gridLayout_2.addWidget(self.sequence_output_filename_button, 2, 2, 1, 1)
        self.sequence_test_filter_button = QtWidgets.QToolButton(self.tab_imagesequence)
        self.sequence_test_filter_button.setEnabled(False)
        self.sequence_test_filter_button.setIcon(icon2)
        self.sequence_test_filter_button.setObjectName("sequence_test_filter_button")
        self.gridLayout_2.addWidget(self.sequence_test_filter_button, 1, 2, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sequence_groupbox = QtWidgets.QGroupBox(self.tab_imagesequence)
        self.sequence_groupbox.setObjectName("sequence_groupbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.sequence_groupbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.sequence_groupbox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.sequence_fpb_spin = QtWidgets.QDoubleSpinBox(self.sequence_groupbox)
        self.sequence_fpb_spin.setPrefix("")
        self.sequence_fpb_spin.setMinimum(0.1)
        self.sequence_fpb_spin.setSingleStep(0.01)
        self.sequence_fpb_spin.setProperty("value", 4.0)
        self.sequence_fpb_spin.setObjectName("sequence_fpb_spin")
        self.horizontalLayout_4.addWidget(self.sequence_fpb_spin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.sequence_groupbox)
        self.sequence_start_button = QtWidgets.QPushButton(self.tab_imagesequence)
        self.sequence_start_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sequence_start_button.sizePolicy().hasHeightForWidth())
        self.sequence_start_button.setSizePolicy(sizePolicy)
        self.sequence_start_button.setIcon(icon3)
        self.sequence_start_button.setObjectName("sequence_start_button")
        self.verticalLayout.addWidget(self.sequence_start_button)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        self.tab_moviemaker.addTab(self.tab_imagesequence, "")
        self.tab_concatenate = QtWidgets.QWidget()
        self.tab_concatenate.setObjectName("tab_concatenate")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_concatenate)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.tab_concatenate)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.join_video1_path_text = QtWidgets.QLineEdit(self.groupBox)
        self.join_video1_path_text.setMinimumSize(QtCore.QSize(200, 0))
        self.join_video1_path_text.setObjectName("join_video1_path_text")
        self.gridLayout.addWidget(self.join_video1_path_text, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.join_video2_path_text = QtWidgets.QLineEdit(self.groupBox)
        self.join_video2_path_text.setMinimumSize(QtCore.QSize(200, 0))
        self.join_video2_path_text.setObjectName("join_video2_path_text")
        self.gridLayout.addWidget(self.join_video2_path_text, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.join_open_video2_button = QtWidgets.QToolButton(self.groupBox)
        self.join_open_video2_button.setIcon(icon1)
        self.join_open_video2_button.setObjectName("join_open_video2_button")
        self.gridLayout.addWidget(self.join_open_video2_button, 1, 2, 1, 1)
        self.join_open_video1_button = QtWidgets.QToolButton(self.groupBox)
        self.join_open_video1_button.setIcon(icon1)
        self.join_open_video1_button.setObjectName("join_open_video1_button")
        self.gridLayout.addWidget(self.join_open_video1_button, 0, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_concatenate)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.join_outputvideo_path_text = QtWidgets.QLineEdit(self.groupBox_2)
        self.join_outputvideo_path_text.setMinimumSize(QtCore.QSize(200, 0))
        self.join_outputvideo_path_text.setObjectName("join_outputvideo_path_text")
        self.gridLayout_3.addWidget(self.join_outputvideo_path_text, 0, 1, 1, 1)
        self.join_open_output_video_button = QtWidgets.QToolButton(self.groupBox_2)
        self.join_open_output_video_button.setIcon(icon1)
        self.join_open_output_video_button.setObjectName("join_open_output_video_button")
        self.gridLayout_3.addWidget(self.join_open_output_video_button, 0, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.join_start_button = QtWidgets.QPushButton(self.tab_concatenate)
        self.join_start_button.setEnabled(False)
        self.join_start_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.join_start_button.setIcon(icon3)
        self.join_start_button.setObjectName("join_start_button")
        self.verticalLayout_4.addWidget(self.join_start_button)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.tab_moviemaker.addTab(self.tab_concatenate, "")
        self.verticalLayout_12.addWidget(self.tab_moviemaker)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.progressbar_label = QtWidgets.QLabel(self.centralwidget)
        self.progressbar_label.setObjectName("progressbar_label")
        self.verticalLayout_6.addWidget(self.progressbar_label)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.verticalLayout_12.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.messagewindow = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messagewindow.setMinimumSize(QtCore.QSize(750, 250))
        self.messagewindow.setReadOnly(True)
        self.messagewindow.setObjectName("messagewindow")
        self.verticalLayout_8.addWidget(self.messagewindow)
        self.verticalLayout_12.addLayout(self.verticalLayout_8)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_10.setBuddy(self.converter_input_path_text)
        self.label_11.setBuddy(self.converter_file_filter_text)
        self.label_13.setBuddy(self.converter_output_format_combobox)
        self.label_12.setBuddy(self.converter_output_path_text)
        self.label.setBuddy(self.sequence_image_path_text)
        self.label_2.setBuddy(self.sequence_image_filter_text)
        self.label_3.setBuddy(self.sequence_output_filename_text)
        self.label_4.setBuddy(self.sequence_fpb_spin)
        self.label_8.setBuddy(self.join_video2_path_text)
        self.label_7.setBuddy(self.join_video1_path_text)
        self.label_9.setBuddy(self.join_outputvideo_path_text)
        self.label_6.setBuddy(self.messagewindow)

        self.retranslateUi(MainWindow)
        self.tab_moviemaker.setCurrentIndex(0)
        self.converter_output_format_combobox.setCurrentIndex(0)
        self.sequence_input_open_folder_button.clicked.connect(MainWindow.sequence_open_input_folder)
        self.sequence_output_filename_button.clicked.connect(MainWindow.sequence_open_output_file)
        self.join_open_video1_button.clicked.connect(MainWindow.join_open_video1)
        self.join_open_video2_button.clicked.connect(MainWindow.join_open_video2)
        self.join_open_output_video_button.clicked.connect(MainWindow.join_open_output_video)
        self.sequence_test_filter_button.clicked.connect(MainWindow.sequence_test_filter)
        self.sequence_image_path_text.editingFinished.connect(MainWindow.sequence_validate_start)
        self.sequence_image_filter_text.editingFinished.connect(MainWindow.sequence_validate_start)
        self.sequence_output_filename_text.editingFinished.connect(MainWindow.sequence_validate_start)
        self.converter_input_path_button.clicked.connect(MainWindow.converter_open_input_folder)
        self.converter_test_filter_button.clicked.connect(MainWindow.converter_test_filter)
        self.converter_output_path_button.clicked.connect(MainWindow.converter_open_output_folder)
        self.converter_input_path_text.editingFinished.connect(MainWindow.converter_validate_start)
        self.converter_file_filter_text.editingFinished.connect(MainWindow.converter_validate_start)
        self.converter_output_path_text.editingFinished.connect(MainWindow.converter_validate_start)
        self.converter_output_format_combobox.currentIndexChanged['QString'].connect(MainWindow.converter_validate_start)
        self.sequence_fpb_spin.valueChanged['double'].connect(MainWindow.sequence_validate_start)
        self.join_video1_path_text.editingFinished.connect(MainWindow.join_validate_start)
        self.join_video2_path_text.editingFinished.connect(MainWindow.join_validate_start)
        self.join_outputvideo_path_text.editingFinished.connect(MainWindow.join_validate_start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tab_moviemaker, self.converter_input_path_text)
        MainWindow.setTabOrder(self.converter_input_path_text, self.converter_input_path_button)
        MainWindow.setTabOrder(self.converter_input_path_button, self.converter_file_filter_text)
        MainWindow.setTabOrder(self.converter_file_filter_text, self.converter_test_filter_button)
        MainWindow.setTabOrder(self.converter_test_filter_button, self.converter_output_format_combobox)
        MainWindow.setTabOrder(self.converter_output_format_combobox, self.converter_output_path_text)
        MainWindow.setTabOrder(self.converter_output_path_text, self.converter_output_path_button)
        MainWindow.setTabOrder(self.converter_output_path_button, self.converter_start_button)
        MainWindow.setTabOrder(self.converter_start_button, self.sequence_image_path_text)
        MainWindow.setTabOrder(self.sequence_image_path_text, self.sequence_input_open_folder_button)
        MainWindow.setTabOrder(self.sequence_input_open_folder_button, self.sequence_image_filter_text)
        MainWindow.setTabOrder(self.sequence_image_filter_text, self.sequence_test_filter_button)
        MainWindow.setTabOrder(self.sequence_test_filter_button, self.sequence_output_filename_text)
        MainWindow.setTabOrder(self.sequence_output_filename_text, self.sequence_output_filename_button)
        MainWindow.setTabOrder(self.sequence_output_filename_button, self.sequence_fpb_spin)
        MainWindow.setTabOrder(self.sequence_fpb_spin, self.sequence_start_button)
        MainWindow.setTabOrder(self.sequence_start_button, self.join_video1_path_text)
        MainWindow.setTabOrder(self.join_video1_path_text, self.join_open_video1_button)
        MainWindow.setTabOrder(self.join_open_video1_button, self.join_video2_path_text)
        MainWindow.setTabOrder(self.join_video2_path_text, self.join_open_video2_button)
        MainWindow.setTabOrder(self.join_open_video2_button, self.join_outputvideo_path_text)
        MainWindow.setTabOrder(self.join_outputvideo_path_text, self.join_open_output_video_button)
        MainWindow.setTabOrder(self.join_open_output_video_button, self.messagewindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MovieMaker"))
        self.label_10.setText(_translate("MainWindow", "Input folder"))
        self.converter_input_path_text.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Input directory</span></p></body></html>"))
        self.converter_input_path_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Open a file dialog window</span></p><p>And select the directory containing the input files you want to convert</p></body></html>"))
        self.converter_input_path_button.setText(_translate("MainWindow", "..."))
        self.label_11.setText(_translate("MainWindow", "File filter"))
        self.converter_file_filter_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use wildcards (* and ?) to define your selection filter</p></body></html>"))
        self.converter_file_filter_text.setText(_translate("MainWindow", "*.tif"))
        self.converter_test_filter_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Check if the filter is matching your selection.</span></p><p>A list of selected files is displayed in the log window.</p></body></html>"))
        self.converter_test_filter_button.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "Output format"))
        self.converter_output_format_combobox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select the output file format</p></body></html>"))
        self.converter_output_format_combobox.setItemText(0, _translate("MainWindow", "JPEG", "JPG"))
        self.converter_output_format_combobox.setItemText(1, _translate("MainWindow", "PNG", "PNG"))
        self.label_12.setText(_translate("MainWindow", "Output folder"))
        self.converter_output_path_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Output folder</p></body></html>"))
        self.converter_output_path_button.setText(_translate("MainWindow", "..."))
        self.converter_start_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Start the batch conversion</p></body></html>"))
        self.converter_start_button.setText(_translate("MainWindow", "Start"))
        self.tab_moviemaker.setTabText(self.tab_moviemaker.indexOf(self.tab), _translate("MainWindow", "Batch image converter"))
        self.label.setText(_translate("MainWindow", "Input folder"))
        self.sequence_image_path_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Folder containig the images to build the video sequence</p></body></html>"))
        self.sequence_input_open_folder_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open a file dialog window to select the input folder</p></body></html>"))
        self.sequence_input_open_folder_button.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Image filter"))
        self.sequence_image_filter_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use wildcards (* and ?) to filter the files in the input folder.</p></body></html>"))
        self.sequence_image_filter_text.setText(_translate("MainWindow", "*.jpeg"))
        self.label_3.setText(_translate("MainWindow", "Output video filename"))
        self.sequence_output_filename_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Filename of the output image sequence movie.</p></body></html>"))
        self.sequence_output_filename_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open a file dialog window to select the output file name</p></body></html>"))
        self.sequence_output_filename_button.setText(_translate("MainWindow", "..."))
        self.sequence_test_filter_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Check the it the filter is matching your selection. </p><p>The output is displayed in the log window.</p></body></html>"))
        self.sequence_test_filter_button.setText(_translate("MainWindow", "..."))
        self.sequence_groupbox.setTitle(_translate("MainWindow", "Advanced options"))
        self.label_4.setText(_translate("MainWindow", "FPS"))
        self.sequence_fpb_spin.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select a number of frame to display in a second.</p></body></html>"))
        self.sequence_start_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Start the image sequence composition</p></body></html>"))
        self.sequence_start_button.setText(_translate("MainWindow", "Start"))
        self.tab_moviemaker.setTabText(self.tab_moviemaker.indexOf(self.tab_imagesequence), _translate("MainWindow", "Image sequence"))
        self.groupBox.setTitle(_translate("MainWindow", "Input files"))
        self.join_video1_path_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Filename of the first video</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Second video"))
        self.join_video2_path_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Filename of the second video</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "First video"))
        self.join_open_video2_button.setText(_translate("MainWindow", "..."))
        self.join_open_video1_button.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output file"))
        self.label_9.setText(_translate("MainWindow", "Output video"))
        self.join_outputvideo_path_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Filename of the output video</p></body></html>"))
        self.join_open_output_video_button.setText(_translate("MainWindow", "..."))
        self.join_start_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Start to join the videos</p></body></html>"))
        self.join_start_button.setText(_translate("MainWindow", "Start"))
        self.tab_moviemaker.setTabText(self.tab_moviemaker.indexOf(self.tab_concatenate), _translate("MainWindow", "Concatenate videos"))
        self.progressbar_label.setText(_translate("MainWindow", "Progress"))
        self.label_6.setText(_translate("MainWindow", "Log window"))

import resource_rc
