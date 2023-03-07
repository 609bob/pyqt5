import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt


class Drawing(QWidget):
    def __init__(self):
        super(Drawing, self).__init__()
        self.setWindowTitle('绘图应用')
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()

    def initUI(self):
        self.resize(600, 600)
        self.pix = QPixmap(600, 600)  #设置画布大小
        self.pix.fill(Qt.white)  #设置背景色为白色

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        pp.drawLine(self.lastPoint, self.endPoint)  #根据鼠标指针前后两个位置绘制直线
        self.lastPoint = self.endPoint  #让前一个坐标值等于后一个坐标值，这样就能实现画出连续的线
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()


    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Drawing()
    main.show()
    sys.exit(app.exec_())

