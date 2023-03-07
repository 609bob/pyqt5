import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie


class LoadingGif(QWidget):
    def __init__(self):
        super(LoadingGif, self).__init__()
        self.label = QLabel(' ', self)
        self.resize(600, 600)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie('./load.gif')
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LoadingGif()
    main.show()
    sys.exit(app.exec_())

