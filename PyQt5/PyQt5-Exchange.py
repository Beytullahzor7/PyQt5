import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QLineEdit, QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.doviz1 = QLineEdit()
        self.label1 = QLabel("Döviz 1")
        self.doviz2 = QLineEdit()
        self.label2 = QLabel("Döviz 2")
        self.amount = QLineEdit()
        self.label3 = QLabel("Amount")
        self.result = QLabel()
        self.button1 = QPushButton("Calculate")

        v_box = QVBoxLayout()
        v_box.addWidget(self.label1)
        v_box.addWidget(self.doviz1)
        v_box.addWidget(self.label2)
        v_box.addWidget(self.doviz2)
        v_box.addWidget(self.label3)
        v_box.addWidget(self.amount)
        v_box.addWidget(self.result)
        v_box.addWidget(self.button1)

        self.setLayout(v_box)

        self.setWindowTitle("Exchange")

        self.button1.clicked.connect(self.calculate)

        self.show()

    def calculate(self):
        url = "http://api.frankfurter.app/latest?from="
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        birim = soup.find_all("span", {"class": "name"})
        deger = soup.find_all("span", {"class": "value"})

        birimler = []
        degerler = []

        for a in birim:
            birimler.append(a.text)
        for b in deger:
            degerler.append((b.text).replace(",", "."))

        if self.doviz1.text() == "TR" and self.doviz2.text() == "EURO":
            amount = int(self.amount.text())
            res = amount * float(degerler[2])
            self.result.setText("Result: " + res)

        if self.doviz1.text() == "TR" and self.doviz2.text() == "USD":
            amount = int(self.amount.text())
            res = amount / float(degerler[1])
            self.result.setText("Result: " + res)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())