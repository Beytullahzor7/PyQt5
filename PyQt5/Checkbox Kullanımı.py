import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout



class Pencere(QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.checkbox = QCheckBox("Python'u seviyor musunuz?")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Bana Tıkla")


        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("Check Box")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))
        #lambda komutunu koyarak fonksiyon objesine dönüştürdük eger koymazsak hata alcaktık
        #lambdayı koymayıp yazsaydık fonksiyon objesi degilde fonksiyon cagrısı olusturmus olurduk

        self.show()

    def click (self, checkbox, yazi_alani):
        if checkbox:
            yazi_alani.setText("Python'u Seviyorsun Cok Güzel...")
        else:
            yazi_alani.setText("Niye Sevmiyorsun ? ")




app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())







