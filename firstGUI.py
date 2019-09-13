import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = uic.loadUi(r"C:\Users\vektorel\Documents\GitHub\Python10DesktopProject\Python10DesktopProje\firstGUI.ui")
        self.pencere.Bt1.clicked.connect(self.tikla)
        self.pencere.show()

    def tikla(self):
        print(self.pencere.txt1.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


