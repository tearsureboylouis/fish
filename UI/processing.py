# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'processing.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)


class ProcessingWindowUI(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(397, 113)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_process = QLabel(Form)
        self.label_process.setObjectName(u"label_process")
        font = QFont()
        font.setWeight(QFont.Thin)
        self.label_process.setFont(font)

        self.verticalLayout.addWidget(self.label_process)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(40, 20))
        font1 = QFont()
        font1.setBold(False)
        self.progressBar.setFont(font1)
        self.progressBar.setCursor(QCursor(Qt.ArrowCursor))
        self.progressBar.setStyleSheet(u"        QProgressBar::chunk {\n"
                                       "            border-radius:10px;\n"
                                       "            background:rgb(53,116,240);\n"
                                       "        }\n"
                                       "         QProgressBar#progressBar {\n"
                                       "            height:20px;\n"
                                       "            text-align:center;\n"
                                       "            font-size:10px;\n"
                                       "            color:white;\n"
                                       "            border-radius:10px;\n"
                                       "            background: #4E5054;\n"
                                       "        }")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_finish = QPushButton(Form)
        self.pushButton_finish.setObjectName(u"pushButton_finish")
        self.pushButton_finish.setEnabled(True)
        self.pushButton_finish.setMinimumSize(QSize(0, 30))
        self.pushButton_finish.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_finish.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButton_finish.setAcceptDrops(False)
        self.pushButton_finish.setCheckable(False)

        self.horizontalLayout.addWidget(self.pushButton_finish)

        self.pushButton_cencel = QPushButton(Form)
        self.pushButton_cencel.setObjectName(u"pushButton_cencel")
        self.pushButton_cencel.setEnabled(True)
        self.pushButton_cencel.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.pushButton_cencel)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        self.pushButton_finish.setDefault(False)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_process.setText(QCoreApplication.translate("Form", u"\u8bf7\u70b9\u51fb\u5f00\u59cb", None))
        self.label.setText(QCoreApplication.translate("Form", u"", None))
        self.pushButton_finish.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.pushButton_cencel.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
    # retranslateUi
