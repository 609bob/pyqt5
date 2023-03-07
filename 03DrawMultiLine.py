import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('绘制不同类型发直线')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        pen = QPen(Qt.red, 3, Qt.SolidLine)  #设置实线

        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashDotDotLine)  #设置虚线
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashLine)  # 设置虚线
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)  # 设置虚线
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)


        painter.end()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())
