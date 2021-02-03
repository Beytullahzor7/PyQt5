import sys

from PyQt5 import QtWidgets

def Pencere():  #butonların sag en altta sabit kalması için iç içe fonk kullanacagız
    #bunun içinde h_box layoutu v_box layout içine yerleştirecegiz

    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addStretch() #butonları saga yasladık en üste koyarak
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)


    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt Ders 5 Devamı")

    pencere.setLayout(v_box)
    pencere.setGeometry(100, 100, 500, 500)

    pencere.show()
    sys.exit(app.exec_())

Pencere()






