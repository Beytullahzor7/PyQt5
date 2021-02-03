import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    v_box = QtWidgets.QVBoxLayout()

    v_box.addWidget(okay)
    v_box.addWidget(cancel)
    v_box.addStretch()

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt Ders 5 Devamı")


    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)

    pencere.show()
    sys.exit(app.exec_())

Pencere()
