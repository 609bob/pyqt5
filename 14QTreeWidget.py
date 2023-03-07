'''
树控件（QTreeWidget)的基本用法
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super(BasicTreeWidget, self).__init__()
        self.setWindowTitle('树控件（QTreeWidget)的基本用法')
        self.tree = QTreeWidget()

        #为树控件指定列数
        self.tree.setColumnCount(2)

        #指定列标签
        self.tree.setHeaderLabels(['Key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setIcon(0, QIcon('./images2/1.png'))
        self.tree.setColumnWidth(0, 120)

        #添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('./images/play.png'))
        child1.setCheckState(0, Qt.Checked)

        self.setCentralWidget(self.tree)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BasicTreeWidget()
    main.show()
    sys.exit(app.exec_())
