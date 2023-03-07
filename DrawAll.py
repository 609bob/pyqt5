'''
绘制各种图形

  弧
  圆形
  椭圆
  矩形
  多边形
  绘制图像
'''


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300, 600)
        self.setWindowTitle('绘制各种图形')

    def painterEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(Qt.blue)

        #绘制弧
        rect = QRect(0, 10, 100, 100)
        # alen: 1个alen等于1/16度  45*16 表示45度
        qp.drawArc(rect, 0, 50*16)

        qp.setPen(Qt.red)
        qp.drawArc(120, 10, 100, 100, 0, 360*16)

        qp.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()
    sys.exit(app.exec_())


