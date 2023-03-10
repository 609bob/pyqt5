import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5, 30, 1355, 730)
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()

        url = os.getcwd() + '/test.html'
        self.layout.addWidget(self.browser)

        button = QPushButton('设置全名')
        self.layout.addWidget(button)
        self.setLayout(self.layout)
        self.setCentralWidget(self.browser)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.show()
    sys.exit(app.exec_())

