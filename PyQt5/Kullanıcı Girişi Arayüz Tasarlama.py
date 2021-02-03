import sys
import sqlite3  # def init altına baglantı olusturduk ver bunu tanımlayarak sqlite3 veri tabanına bagladık
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()

        self.init_ui()

    def baglanti_olustur(self):

        baglanti = sqlite3.connect("database1.db")

        self.cursor = baglanti.cursor() #veritabanı üzerinde işlemler gerçekleştirmek için kullandık

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Uyeler (Kullanıcı_adı TEXT,Parola TEXT)")

        baglanti.commit()

    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)  # PAROLAYI GİRERKEN GÖZÜKMEMESİ İÇİN BUNU KULLANDIK
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)

        self.show()

    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From Uyeler where kullanıcı_adı = ? and parola = ?", (adi, par))
        data = self.cursor.fetchall()  # sorgudan dönen degerleri almak için bu komutu kullandık

        if len(data) == 0:
            self.yazi_alani.setText("Böyle Bir Kullanıcı Yok\nLütfen Tekrar Deneyiniz...")

        else:
            self.yazi_alani.setText("Hosgeldiniz " + adi)


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
