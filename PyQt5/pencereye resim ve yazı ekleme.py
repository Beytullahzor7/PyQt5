import sys

from PyQt5 import QtWidgets,QtGui #pencere buton gibi özellikleri barındıran bir dosya

def Pencere():

    app = QtWidgets.QApplication(sys.argv) #pyqt5 içinde mutlaka app yer almalı

    pencere = QtWidgets.QWidget() #PENCERE OBJEMİZ OLUSTU
    pencere.setWindowTitle("PyQt5 Ders 2") #pencere baslıgını değiştirdik

    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)

    etiket1.setText("Burası Bir Yazıdır.")
    etiket2.setPixmap(QtGui.QPixmap("indir.png")) #pencere içerisine resim eklemek qtgui içindeki classları kullandık

    etiket1.move(200, 75)
    etiket2.move(100, 100)


    pencere.setGeometry(100, 100, 500, 500) #pencerenin olusacagı yeri kendim belirledim
    pencere.show()

    sys.exit(app.exec_()) #biz carpıya basmayana kadar pencere acık kalsın komutu

Pencere()



