'''
Created on 2021/02/13

@author: Mamoru
'''
import sys
from PyQt5.QtCore import pyqtSlot
from  PyQt5.QtWidgets import QApplication,QMainWindow
import os
sys.path.append(os.path.abspath("."))

from .ui_test import *

class GUItest(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUItest,self).__init__(parent)
        self.setupUi(self)
        #loadUi('test.ui',self)
        #self.pushButton.clicked.connect(self.onPushButtonCliked)

    #@pyqtSlot()
    #def onPushButtonCliked(self):
    #   self.label1.setText(self.textEdit.text)

if __name__=="__main__":
    app=QApplication(sys.argv)
    widget=GUItest()
    widget.show()
    sys.exit(app.exec_())

def main():
    app=QApplication(sys.argv)
    widget=GUItest()
    widget.show()
    sys.exit(app.exec_())


