import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.brouser = QWebEngineView()
        self.setWindowIcon(QtGui.QIcon('icons8.png'))
        # self.setWindowFlags(Qt.Tool)
        self.brouser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.brouser)
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Brouser')
    window = MainWindow()
    app.exec_()
