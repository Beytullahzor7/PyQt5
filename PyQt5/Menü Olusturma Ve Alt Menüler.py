import sys

from PyQt5.QtWidgets import QApplication,QAction,QMainWindow,qApp

class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Ac",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Cıkıs",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac )
        dosya.addAction(dosya_kaydet)   #bu 3 özelligi dosya nın alt sekmesine ekledik
        dosya.addAction(cikis)

        ara_ve_degistir = duzenle.addMenu("Ara ve Değiştir")

        ara = QAction("Ara",self)
        degistir = QAction("Degistir",self)

        temizle = QAction("Temizle",self)


        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)
        duzenle.addAction(temizle)


        cikis.triggered.connect(self.cikis_yap)
        dosya.triggered.connect(self.response)

        self.setWindowTitle("Menu")
        self.show()

    def cikis_yap(self):
        qApp.quit()

    def response(self,action): #şuanda python kendi içinde aslında bir action objesi gönderdi ancak biz göremiyoruz
        if action.text() == "Dosya Ac":                  #self,action dedigimiz zaman da hangi actiona basıldıgını görebiliriz
            print("Dosya Ac'a Basıldı")

        elif action.text() == "Dosya Kaydet":
            print("Dosya Kaydet'e Basıldı")

        elif action.text() == "Cıkıs":
            print("Cıkıs'a Basıldı")




app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())