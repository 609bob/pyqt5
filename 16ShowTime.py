import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ShowTime(QWidget):
    def __init__(self):
        super(ShowTime, self).__init__()
        self.setWindowTitle("动态显示当前时间")
        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        layout = QGridLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)

        self.setLayout(layout)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)



    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ShowTime()
    main.show()
    QTimer.singleShot(5000, app.quit)  #5秒后窗口自动关闭
    sys.exit(app.exec_())



