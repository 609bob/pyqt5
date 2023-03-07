import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300, 200)

        tb1 = self.addToolBar('File')

        new = QAction(QIcon('./images2/1.png'), 'new', self)
        tb1.addAction(new)

        Open = QAction(QIcon('./images2/10.png'), 'open', self)
        tb1.addAction(Open)

        save = QAction(QIcon('./images2/6.png'), 'save', self)
        tb1.addAction(save)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec_())

