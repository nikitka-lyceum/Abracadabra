import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()
    ex.show()

    sys.exit(app.exec())
