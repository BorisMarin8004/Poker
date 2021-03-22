from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 2000, 1000)
    win.setWindowTitle("Poker")

    label = QtWidgets.QLabel(win)
    label.setText("Poker")
    label.move(1000, 500)

    win.show()
    sys.exit(app.exec_())

window()