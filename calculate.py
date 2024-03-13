from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton,
    QLabel,
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.amallar = ''
        self.setWindowTitle("Calculator")
        self.lbl = QLabel()
        self.btn1 = QPushButton('1')
        self.btn2 = QPushButton('2')
        self.btn3 = QPushButton('3')
        self.btnmult = QPushButton('/')
        self.g = QHBoxLayout()
        self.g.addWidget(self.btn1)
        self.g.addWidget(self.btn2)
        self.g.addWidget(self.btn3)
        self.g.addWidget(self.btnmult)
    
        self.btn4 = QPushButton('4')
        self.btn5 = QPushButton('5')
        self.btn6 = QPushButton('6')
        self.btndigit = QPushButton('*')
        self.g1 = QHBoxLayout()
        self.g1.addWidget(self.btn4)
        self.g1.addWidget(self.btn5)
        self.g1.addWidget(self.btn6)
        self.g1.addWidget(self.btndigit)


        self.btn7 = QPushButton('7')
        self.btn8 = QPushButton('8')
        self.btn9 = QPushButton('9')
        self.btnminus = QPushButton('-')
        self.g2 = QHBoxLayout()
        self.g2.addWidget(self.btn7)
        self.g2.addWidget(self.btn8)
        self.g2.addWidget(self.btn9)
        self.g2.addWidget(self.btnminus)


        self.btn0 = QPushButton('0')
        self.btnbarobar = QPushButton('=')
        self.plus = QPushButton('+')
        self.c = QPushButton("C")
        self.g3 = QHBoxLayout()
        self.g3.addWidget(self.btn0)
        self.g3.addWidget(self.btnbarobar)
        self.g3.addWidget(self.plus)
        self.g3.addWidget(self.c)
        


        self.v = QVBoxLayout()
        self.v.addWidget(self.lbl)
        self.v.addLayout(self.g)
        self.v.addLayout(self.g1)
        self.v.addLayout(self.g2)
        self.v.addLayout(self.g3)
        self.setLayout(self.v)
        self.btn1.clicked.connect(self.printf)
        self.btn2.clicked.connect(self.printf)
        self.btn3.clicked.connect(self.printf)
        self.btn4.clicked.connect(self.printf)
        self.btn5.clicked.connect(self.printf)
        self.btn6.clicked.connect(self.printf)
        self.btn7.clicked.connect(self.printf)
        self.btn8.clicked.connect(self.printf)
        self.btn9.clicked.connect(self.printf)
        self.plus.clicked.connect(self.printf)
        self.btndigit.clicked.connect(self.printf)
        self.btnminus.clicked.connect(self.printf)
        self.btnmult.clicked.connect(self.printf)

        self.c.clicked.connect(self.clearInput)
        self.btnbarobar.clicked.connect(self.calculate)
    

    def printf(self):
        xodisa = self.sender()
        self.amallar = self.amallar + xodisa.text()
        self.lbl.setText(self.amallar)
        
    def clearInput(self):
        self.amallar = ""
        self.lbl.setText("")

    def calculate(self):
        if '+' in self.amallar:
            self.amallar = self.amallar.split('+')
            natija = int(self.amallar[0]) + int(self.amallar[1])
            self.lbl.setText(str(natija))
        elif '-' in self.amallar:
            self.amallar = self.amallar.split('-')
            natija = int(self.amallar[0]) - int(self.amallar[1])
            self.lbl.setText(str(natija))

        elif '*' in self.amallar:
            self.amallar = self.amallar.split('*')
            natija = int( self.amallar[0]) * int(self.amallar[1])
            self.lbl.setText(str(natija))
        
        elif '/' in self.amallar:
            self.amallar = self.amallar.split('/')
            natija = int( self.amallar[0]) // int(self.amallar[1])
            self.lbl.setText(str(natija))

app = QApplication([])
screen = mainWindow()
screen.show()
app.exec()
