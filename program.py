import sys
from random import  randint

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

import random


class Example(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('Ul.ui', self)
        self.initUI()

    def initUI(self):


        self.flag = 0

        self.pushButton.move(30, 30)
        self.pushButton.resize(100, 50)
        self.pushButton.clicked.connect(self.refresh)

    def refresh(self):
        self.flag = 1
        self.update()

    def paintEvent(self, e):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        count = randint(1, 10)
        for i in range(count):
            x = randint(50, 350)
            y = randint(50, 350)
            rad = randint(3, 50)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(x - rad, y - rad, x + rad, y + rad)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
