import os
import sys
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from speech import Ui_Dialog

class Dialog(QDialog):

    def __init__(self):
        super(Dialog, self).__init__()
        loadUi("start.ui", self)
        self.pushButton.clicked.connect(self.start)
        self.newwindow = None

    @pyqtSlot()
    def start(self):
        self.newwindow = Ui_Dialog()
        ui.hide()
        self.newwindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())




