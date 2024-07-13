# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QLabel)


class MainWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(989, 679)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_video = QVBoxLayout()
        self.verticalLayout_video.setSpacing(5)
        self.verticalLayout_video.setObjectName(u"verticalLayout_video")

        self.video_label = QLabel()
        self.video_label.setFixedSize(800, 600)
        self.verticalLayout_video.addWidget(self.video_label)

        self.frame_video_control = QFrame(self.frame)
        self.frame_video_control.setObjectName(u"frame_video_control")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_video_control.sizePolicy().hasHeightForWidth())
        self.frame_video_control.setSizePolicy(sizePolicy)
        self.frame_video_control.setMinimumSize(QSize(0, 40))
        self.frame_video_control.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_video_control.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_video_control)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_player = QHBoxLayout()
        self.horizontalLayout_player.setObjectName(u"horizontalLayout_player")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_player.addItem(self.horizontalSpacer)

        self.pushButton_play = QPushButton(self.frame_video_control)
        self.pushButton_play.setObjectName(u"pushButton_play")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_play.sizePolicy().hasHeightForWidth())
        self.pushButton_play.setSizePolicy(sizePolicy1)
        self.pushButton_play.setMinimumSize(QSize(30, 30))
        icon = QIcon(QIcon.fromTheme(u"media-playback-start"))
        self.pushButton_play.setIcon(icon)
        self.pushButton_play.setIconSize(QSize(20, 20))

        self.horizontalLayout_player.addWidget(self.pushButton_play)

        self.pushButton_purse = QPushButton(self.frame_video_control)
        self.pushButton_purse.setObjectName(u"pushButton_purse")
        sizePolicy1.setHeightForWidth(self.pushButton_purse.sizePolicy().hasHeightForWidth())
        self.pushButton_purse.setSizePolicy(sizePolicy1)
        self.pushButton_purse.setMinimumSize(QSize(30, 30))
        icon1 = QIcon(QIcon.fromTheme(u"media-playback-pause"))
        self.pushButton_purse.setIcon(icon1)
        self.pushButton_purse.setIconSize(QSize(20, 20))

        self.horizontalLayout_player.addWidget(self.pushButton_purse)

        self.pushButton_reset = QPushButton(self.frame_video_control)
        self.pushButton_reset.setObjectName(u"pushButton__reset")
        sizePolicy1.setHeightForWidth(self.pushButton_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_reset.setSizePolicy(sizePolicy1)
        self.pushButton_reset.setMinimumSize(QSize(30, 30))
        icon2 = QIcon(QIcon.fromTheme(u"view-restore"))
        self.pushButton_reset.setIcon(icon2)
        self.pushButton_reset.setIconSize(QSize(20, 20))

        self.horizontalLayout_player.addWidget(self.pushButton_reset)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_player.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_player)

        self.verticalLayout_video.addWidget(self.frame_video_control)

        self.horizontalLayout.addLayout(self.verticalLayout_video)

        self.verticalLayout_layer_list = QVBoxLayout()
        self.verticalLayout_layer_list.setSpacing(5)
        self.verticalLayout_layer_list.setObjectName(u"verticalLayout_layer_list")
        self.verticalLayout_layer_list.setContentsMargins(0, 0, 5, 0)

        self.horizontalLayout.addLayout(self.verticalLayout_layer_list)

        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
