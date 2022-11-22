import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.is_paint = False

        self.button.clicked.connect(self.paint)

    def paint(self):
        self.is_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.is_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        for _ in range(10):
            # Задаем кисть
            qp.setBrush(QColor(255, 255, 0))
            r = random.randint(5, 150)
            x_win, y_win = self.geometry().x(), self.geometry().y()
            x, y = random.randint(20, x_win - 20 - r - r), random.randint(20, y_win - 20 - r - r)
            qp.drawEllipse(x, y, r, r)

        self.is_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()
    ex.show()

    sys.exit(app.exec())
