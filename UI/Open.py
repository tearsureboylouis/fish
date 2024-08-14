# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Open.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
                               QWidget)


class OpenWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModality.NonModal)
        Form.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setKerning(True)
        Form.setFont(font)
        Form.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_window = QFrame(Form)
        self.main_window.setObjectName(u"main_window")
        self.main_window.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_window.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.main_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(self.main_window)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMaximumSize(QSize(16777215, 40))
        self.frame_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_exit = QPushButton(self.frame_header)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(570, 10, 20, 20))
        self.pushButton_exit.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon(QIcon.fromTheme(u"application-exit"))
        self.pushButton_exit.setIcon(icon)
        self.pushButton_exit.setIconSize(QSize(8, 8))
        self.title = QLabel(self.frame_header)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 51, 21))

        self.verticalLayout.addWidget(self.frame_header)

        self.mian_body = QGridLayout()
        self.mian_body.setSpacing(0)
        self.mian_body.setObjectName(u"mian_body")
        self.pushButton_new_project = QPushButton(self.main_window)
        self.pushButton_new_project.setObjectName(u"pushButton_new_project")
        self.pushButton_new_project.setMinimumSize(QSize(120, 40))
        self.pushButton_new_project.setMaximumSize(QSize(150, 50))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setKerning(True)
        self.pushButton_new_project.setFont(font1)
        self.pushButton_new_project.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_new_project.setStyleSheet(u"")
        self.pushButton_new_project.setIconSize(QSize(18, 18))

        self.mian_body.addWidget(self.pushButton_new_project, 1, 0, 1, 1)

        self.stackedWidget_body = QStackedWidget(self.main_window)
        self.stackedWidget_body.setObjectName(u"stackedWidget_body")
        self.stackedWidget_body.setLineWidth(0)
        self.newProject = QWidget()
        self.newProject.setObjectName(u"newProject")
        self.pushButton_finish = QPushButton(self.newProject)
        self.pushButton_finish.setObjectName(u"pushButton_finish")
        self.pushButton_finish.setGeometry(QRect(380, 462, 75, 31))
        self.layoutWidget = QWidget(self.newProject)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 441, 141))
        self.GridLayout_body = QGridLayout(self.layoutWidget)
        self.GridLayout_body.setObjectName(u"GridLayout_body")
        self.GridLayout_body.setHorizontalSpacing(10)
        self.GridLayout_body.setContentsMargins(0, 0, 0, 0)
        self.pushButton_open_file = QPushButton(self.layoutWidget)
        self.pushButton_open_file.setObjectName(u"pushButton_open_file")
        self.pushButton_open_file.setMinimumSize(QSize(30, 30))
        icon1 = QIcon(QIcon.fromTheme(u"document-new"))
        self.pushButton_open_file.setIcon(icon1)
        self.pushButton_open_file.setIconSize(QSize(16, 16))

        self.GridLayout_body.addWidget(self.pushButton_open_file, 2, 2, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.GridLayout_body.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(0, 30))
        self.lineEdit_name.setFont(font1)

        self.GridLayout_body.addWidget(self.lineEdit_name, 0, 1, 1, 1)

        self.pushButton_open_folder = QPushButton(self.layoutWidget)
        self.pushButton_open_folder.setObjectName(u"pushButton_open_folder")
        self.pushButton_open_folder.setMinimumSize(QSize(30, 30))
        self.pushButton_open_folder.setFont(font1)
        icon2 = QIcon(QIcon.fromTheme(u"folder"))
        self.pushButton_open_folder.setIcon(icon2)
        self.pushButton_open_folder.setIconSize(QSize(16, 16))

        self.GridLayout_body.addWidget(self.pushButton_open_folder, 1, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.GridLayout_body.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_video = QLineEdit(self.layoutWidget)
        self.lineEdit_video.setObjectName(u"lineEdit_video")
        self.lineEdit_video.setMinimumSize(QSize(0, 30))
        self.lineEdit_video.setFont(font1)

        self.GridLayout_body.addWidget(self.lineEdit_video, 2, 1, 1, 1)

        self.lineEdit_path = QLineEdit(self.layoutWidget)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setMinimumSize(QSize(0, 30))
        self.lineEdit_path.setFont(font1)

        self.GridLayout_body.addWidget(self.lineEdit_path, 1, 1, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setFont(font1)

        self.GridLayout_body.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayoutWidget = QWidget(self.newProject)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 170, 441, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_water_depth = QLabel(self.gridLayoutWidget)
        self.label_water_depth.setObjectName(u"label_water_depth")
        self.label_water_depth.setFont(font1)

        self.gridLayout.addWidget(self.label_water_depth, 0, 0, 1, 1)

        self.lineEdit_water_depth = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_water_depth.setObjectName(u"lineEdit_water_depth")
        self.lineEdit_water_depth.setMinimumSize(QSize(0, 30))
        self.lineEdit_water_depth.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_water_depth, 0, 1, 1, 1)

        self.label_time = QLabel(self.gridLayoutWidget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font1)

        self.gridLayout.addWidget(self.label_time, 0, 2, 1, 1)

        self.lineEdit_time = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_time.setObjectName(u"lineEdit_time")
        self.lineEdit_time.setMinimumSize(QSize(0, 30))
        self.lineEdit_time.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_time, 0, 3, 1, 1)

        self.stackedWidget_body.addWidget(self.newProject)
        self.recordingPage = QWidget()
        self.recordingPage.setObjectName(u"recordingPage")
        self.verticalLayout_2 = QVBoxLayout(self.recordingPage)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_project_setting = QLabel(self.recordingPage)
        self.label_project_setting.setObjectName(u"label_project_setting")
        self.label_project_setting.setFont(font1)
        self.label_project_setting.setMargin(10)

        self.verticalLayout_4.addWidget(self.label_project_setting)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.lineEdit_save_path_r = QLineEdit(self.recordingPage)
        self.lineEdit_save_path_r.setObjectName(u"lineEdit_save_path_r")
        self.lineEdit_save_path_r.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.lineEdit_save_path_r, 1, 1, 1, 1)

        self.label_save_path_r = QLabel(self.recordingPage)
        self.label_save_path_r.setObjectName(u"label_save_path_r")
        self.label_save_path_r.setFont(font1)

        self.gridLayout_3.addWidget(self.label_save_path_r, 1, 0, 1, 1)

        self.lineEdit_project_name_r = QLineEdit(self.recordingPage)
        self.lineEdit_project_name_r.setObjectName(u"lineEdit_project_name_r")
        self.lineEdit_project_name_r.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.lineEdit_project_name_r, 0, 1, 1, 1)

        self.label_project_name_r = QLabel(self.recordingPage)
        self.label_project_name_r.setObjectName(u"label_project_name_r")
        self.label_project_name_r.setFont(font1)

        self.gridLayout_3.addWidget(self.label_project_name_r, 0, 0, 1, 1)

        self.pushButton_save_path_r = QPushButton(self.recordingPage)
        self.pushButton_save_path_r.setObjectName(u"pushButton_save_path_r")
        self.pushButton_save_path_r.setMinimumSize(QSize(30, 30))
        self.pushButton_save_path_r.setMaximumSize(QSize(30, 16777215))
        icon3 = QIcon(QIcon.fromTheme(u"document-save"))
        self.pushButton_save_path_r.setIcon(icon3)
        self.pushButton_save_path_r.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.pushButton_save_path_r, 1, 2, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.label_recording_setting = QLabel(self.recordingPage)
        self.label_recording_setting.setObjectName(u"label_recording_setting")
        self.label_recording_setting.setFont(font1)
        self.label_recording_setting.setMargin(10)

        self.verticalLayout_4.addWidget(self.label_recording_setting)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.comboBox_body_r = QComboBox(self.recordingPage)
        self.comboBox_body_r.setObjectName(u"comboBox_body_r")
        self.comboBox_body_r.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_body_r, 0, 1, 1, 1)

        self.label_water_deep_r = QLabel(self.recordingPage)
        self.label_water_deep_r.setObjectName(u"label_water_deep_r")
        self.label_water_deep_r.setFont(font1)

        self.gridLayout_4.addWidget(self.label_water_deep_r, 1, 0, 1, 1)

        self.lineEdit_water_deep_r = QLineEdit(self.recordingPage)
        self.lineEdit_water_deep_r.setObjectName(u"lineEdit_water_deep_r")
        self.lineEdit_water_deep_r.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_water_deep_r, 1, 1, 1, 1)

        self.label_body_r = QLabel(self.recordingPage)
        self.label_body_r.setObjectName(u"label_body_r")
        self.label_body_r.setFont(font1)

        self.gridLayout_4.addWidget(self.label_body_r, 0, 0, 1, 1)

        self.pushButton_refresh = QPushButton(self.recordingPage)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setMinimumSize(QSize(30, 30))
        icon4 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.pushButton_refresh.setIcon(icon4)
        self.pushButton_refresh.setIconSize(QSize(15, 15))

        self.gridLayout_4.addWidget(self.pushButton_refresh, 0, 2, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.pushButton_start_recording = QPushButton(self.recordingPage)
        self.pushButton_start_recording.setObjectName(u"pushButton_start_recording")
        self.pushButton_start_recording.setMinimumSize(QSize(100, 40))
        self.pushButton_start_recording.setMaximumSize(QSize(100, 40))
        self.pushButton_start_recording.setFont(font1)

        self.gridLayout_6.addWidget(self.pushButton_start_recording, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_6)

        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.stackedWidget_body.addWidget(self.recordingPage)
        self.openProject = QWidget()
        self.openProject.setObjectName(u"openProject")
        self.verticalLayout_3 = QVBoxLayout(self.openProject)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, -1)
        self.label_7 = QLabel(self.openProject)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_7)

        self.gridLayout_recently = QGridLayout()
        self.gridLayout_recently.setObjectName(u"gridLayout_recently")

        self.verticalLayout_3.addLayout(self.gridLayout_recently)

        self.label_8 = QLabel(self.openProject)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.openProject)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setFont(font1)

        self.horizontalLayout.addWidget(self.label_9)

        self.lineEdit_xml_file = QLineEdit(self.openProject)
        self.lineEdit_xml_file.setObjectName(u"lineEdit_xml_file")
        self.lineEdit_xml_file.setMinimumSize(QSize(0, 30))
        self.lineEdit_xml_file.setFont(font1)
        self.lineEdit_xml_file.setReadOnly(False)

        self.horizontalLayout.addWidget(self.lineEdit_xml_file)

        self.pushButton_choose_xml = QPushButton(self.openProject)
        self.pushButton_choose_xml.setObjectName(u"pushButton_choose_xml")
        self.pushButton_choose_xml.setMinimumSize(QSize(0, 30))
        self.pushButton_choose_xml.setFont(font1)
        self.pushButton_choose_xml.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.pushButton_choose_xml)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.openProject)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.stackedWidget_body.addWidget(self.openProject)

        self.mian_body.addWidget(self.stackedWidget_body, 0, 1, 7, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.mian_body.addItem(self.verticalSpacer, 3, 0, 4, 1)

        self.pushButton_recording = QPushButton(self.main_window)
        self.pushButton_recording.setObjectName(u"pushButton_recording")
        self.pushButton_recording.setMinimumSize(QSize(120, 40))
        self.pushButton_recording.setMaximumSize(QSize(150, 50))
        self.pushButton_recording.setFont(font1)

        self.mian_body.addWidget(self.pushButton_recording, 2, 0, 1, 1)

        self.pushButton_open_project = QPushButton(self.main_window)
        self.pushButton_open_project.setObjectName(u"pushButton_open_project")
        self.pushButton_open_project.setMinimumSize(QSize(40, 0))
        self.pushButton_open_project.setMaximumSize(QSize(200, 50))
        self.pushButton_open_project.setFont(font1)
        self.pushButton_open_project.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_open_project.setIconSize(QSize(20, 20))

        self.mian_body.addWidget(self.pushButton_open_project, 0, 0, 1, 1)

        self.verticalLayout.addLayout(self.mian_body)

        self.frame_footer = QFrame(self.main_window)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMaximumSize(QSize(16777215, 40))
        self.frame_footer.setSizeIncrement(QSize(0, 0))
        self.frame_footer.setBaseSize(QSize(0, 0))
        self.frame_footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Shadow.Raised)
        self.Version = QPushButton(self.frame_footer)
        self.Version.setObjectName(u"Version")
        self.Version.setGeometry(QRect(540, 10, 51, 21))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setKerning(True)
        self.Version.setFont(font2)
        # self.Version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.frame_footer)

        self.gridLayout_2.addWidget(self.main_window, 0, 0, 1, 1)

        self.retranslateUi(Form)

        self.stackedWidget_body.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_exit.setText("")
        self.title.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u9879\u76ee", None))
        self.pushButton_new_project.setText(QCoreApplication.translate("Form", u"\u65b0\u5efa\u9879\u76ee", None))
        self.pushButton_finish.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210", None))
        self.pushButton_open_file.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u89c6\u9891\uff1a", None))
        self.pushButton_open_folder.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u540d\u79f0\uff1a", None))
        self.label_water_depth.setText(QCoreApplication.translate("Form", u"\u6c34\u6df1\uff08cm\uff09", None))
        self.label_time.setText(QCoreApplication.translate("Form", u"\u65f6\u957f\uff08s\uff09", None))
        self.label_project_setting.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u8bbe\u7f6e", None))
        self.label_save_path_r.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.label_project_name_r.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u540d\u79f0", None))
        self.pushButton_save_path_r.setText("")
        self.label_recording_setting.setText(QCoreApplication.translate("Form", u"\u5f55\u5236\u8bbe\u7f6e", None))
        self.label_water_deep_r.setText(QCoreApplication.translate("Form", u"\u6c34\u6df1\uff08cm\uff09", None))
        self.label_body_r.setText(QCoreApplication.translate("Form", u"\u5f55\u5236\u7a97\u4f53", None))
        self.pushButton_refresh.setText("")
        self.pushButton_start_recording.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5f55\u5236", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6700\u8fd1\u9879\u76ee", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u9879\u76ee", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u914d\u7f6e\u6587\u4ef6\uff1a", None))
        self.pushButton_choose_xml.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u9879\u76ee", None))
        self.pushButton_recording.setText(QCoreApplication.translate("Form", u"\u5b9e\u65f6\u8bc6\u522b", None))
        self.pushButton_open_project.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u9879\u76ee", None))
        self.Version.setText(QCoreApplication.translate("Form", u"v1.0.0", None))
    # retranslateUi
