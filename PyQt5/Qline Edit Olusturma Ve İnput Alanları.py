import sys

from PyQt5 import QtWidgets

class Pencere (QtWidgets.QWidget):
    def __init__(self):

        super().__init__() #yukarıda yazdıgımız QWİDGET sınıfını cagırdık

        self.init_ui() #ekstra özellikler eklemek içinde init_ui tanımladım

    def init_ui(self):

        self.yazı_alanı = QtWidgets.QLineEdit() #QLineEdit ile input olusturduk ve artık yazı yazabilecegimiz bir alan var
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdır = QtWidgets.QPushButton("Yazdır!")


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addStretch()  # boşluk bırakmak için yazdık

        self.setLayout(v_box) #v_boxu kendi penceremize ekledik

        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)


        self.show()

    def click(self): #hangi butona basıldıgını anlamam için qwidgets içindeki bir fonk. kullanalım

        sender = self.sender() #eger temizle butonuna basılırsa üzerindeki yazı bana gelicek ve altta olusturacagımız if ile bunu anlayabilecegiz
        # 2 tane buton olusturduk (temizle ve yazdır) hangisine basıldıgını anlamamız için sender fonk. kullanıp if else ile komutunu belirledik

        if sender.text() == "Temizle":

            self.yazı_alanı.clear()

        else:

            print(self.yazı_alanı.text())

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()
sys.exit(app.exec_())