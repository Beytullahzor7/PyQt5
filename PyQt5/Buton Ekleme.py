import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt 3. Ders")

    buton = QtWidgets.QPushButton(pencere) #buton oluşturma metodu
    buton.setText("Burası Bir Butondur")

    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba Dünya")

    etiket.move(200,30)
    buton.move(190,60)


    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()