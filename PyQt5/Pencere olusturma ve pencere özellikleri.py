import sys #komut satırı çalıştırması

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Pyqt 5 Ders 1")

    pencere.setGeometry(100,100,500,500)
    pencere.show()

    sys.exit(app.exec_()) #döngü sürekliliğinin sağlanması

Pencere()