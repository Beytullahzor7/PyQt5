import sys

from PyQt5 import QtWidgets

#PROGRAMLAR DAHA KAPSAMLI OLACAGINDAN DOLAYI ARTIK CLASS KULLANACAGIZ

class Pencere(QtWidgets.QWidget): #penceremizin direkt qtwidgetten miras almasını istedik

    def __init__(self):

        super().__init__() #miras aldıgım qwidgeti bu fonksiyon sayesinde kullandım

        self.init_ui() #ekstra özellik eklemek için koyduk şuan tanımlı degil aşağıda tanımlayacagız

    def init_ui(self):

        self.yazı_alanı = QtWidgets.QLabel("Bana Henüz Tıklanmadı...")
        self.buton = QtWidgets.QPushButton("Bana Tıkla!")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.buton.clicked.connect(self.click) #self.click fonksiyonuna baglandık kullanmak için tanımlamamız lazım

        self.show()

    def click(self):

        self.say += 1
        self.yazı_alanı.setText("Bana " + str(self.say) + " defa Tıklandı!")

        if self.say == 25:
            breakpoint(self.say) #25 kere tıklayınca program kapasın

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())












