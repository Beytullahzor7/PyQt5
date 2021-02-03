import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout() #yatay layout

    h_box.addWidget(okay)
    h_box.addWidget(cancel) #butonlarımı horizontal box içerisine yerleştirdim
    h_box.addStretch() #bu ifade butonları sola yasladı eger addWiget basına koyarsam sola yaslar, ortaya koyarsamda ortaya yaslar

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt Ders 5")

    pencere.setLayout(h_box) #ana penecere içerisine h_box u ekledik
    pencere.setGeometry(100,100,500,500)

    pencere.show()
    sys.exit(app.exec_())

Pencere()

