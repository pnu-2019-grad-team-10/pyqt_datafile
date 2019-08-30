# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from test2_ui import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self, w):
        Ui_MainWindow.__init__(self)
        self.setupUi(w)

    def exitWindow(self):
        app.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = MainWindow(w)
    w.show()
    sys.exit(app.exec_())

