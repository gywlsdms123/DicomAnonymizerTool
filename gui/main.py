# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(503, 135)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.txtFile = QLineEdit(self.frame)
        self.txtFile.setObjectName(u"txtFile")
        self.txtFile.setReadOnly(True)

        self.gridLayout.addWidget(self.txtFile, 0, 1, 1, 1)

        self.btnPath = QToolButton(self.frame)
        self.btnPath.setObjectName(u"btnPath")

        self.gridLayout.addWidget(self.btnPath, 0, 2, 1, 1)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnStart = QPushButton(self.frame)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnStop = QPushButton(self.frame)
        self.btnStop.setObjectName(u"btnStop")

        self.horizontalLayout.addWidget(self.btnStop)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dicom \ud3f4\ub354", None))
        self.btnPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
    # retranslateUi

