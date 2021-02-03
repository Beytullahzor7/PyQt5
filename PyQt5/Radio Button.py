import sys

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.radio_yazısı = QLabel("Hangi Dili Daha Cok Seviyorsunuz?")
        self.java = QRadioButton("JAVA")
        self.python = QRadioButton("PYTHON")
        self.c = QRadioButton("C#")

        self.yazi_alani = QLabel("")
        self.buton = QPushButton("GÖNDER")
        self.yazi_alani.move(250,250)

        v_box = QVBoxLayout()

        v_box.addWidget(self.radio_yazısı)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.c)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)


        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.buton.clicked.connect(lambda : self.click(self.java.isChecked(),self.python.isChecked(),self.c.isChecked(),self.yazi_alani))

        self.setWindowTitle("Radio Button")
        self.show()

    def click(self,java,python,c,yazi_alani):
        if java:
            yazi_alani.setText("Java Secilmiştir.")
        if python:
            yazi_alani.setText("Python Secilmistir.")
        if c:
            yazi_alani.setText("C# Secilmistir.")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())











