# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testgCIwdv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PyQt5.QtCore import *
from  PyQt5.QtWidgets import *
from  PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 100, 75, 23))
        self.textEdit1 = QTextEdit(self.centralwidget)
        self.textEdit1.setObjectName(u"textEdit1")
        self.textEdit1.setGeometry(QRect(200, 20, 104, 71))
        self.textEdit1.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(70, 150, 451, 221))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.onPushButtonCliked)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

    @pyqtSlot()
    def onPushButtonCliked(self):
        print("push")
        self.label1.setText(self.textEdit1.toPlainText())

