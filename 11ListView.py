import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        self.setWindowTitle("QListView例子")
        self.resize(300, 270)
        layout = QVBoxLayout()

        listview = QListView()
        listModel = QStringListModel()
        self.list = ['列表项1', '列表项2', '列表项3']

        listModel.setStringList(self.list)
        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, 'QListView', '您选择了：' + self.list[item.row()])





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListView()
    main.show()
    sys.exit(app.exec_())
