import sys, time
from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication, QLineEdit, QLabel
from PyQt5.QtCore import QSize, Qt, QLine, QPoint
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QThread, pyqtSignal


class Ellipse():
    x = 0
    y = 0
    width = 0
    height = 0
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(800, 600))

        buttonStat = QPushButton("Stát",self)
        buttonStat.clicked.connect(self.draw_circle)
        buttonStat.resize(100,50)
        buttonStat.move(10,10)
        self.circle = None

        buttonPozor = QPushButton("Pozor", self)
        buttonPozor.clicked.connect(self.draw_circle2)
        buttonPozor.resize(100, 50)
        buttonPozor.move(10, 100)
        self.circle2 = None

        buttonJed = QPushButton("Jeď", self)
        buttonJed.clicked.connect(self.draw_circle3)
        buttonJed.resize(100, 50)
        buttonJed.move(10, 200)
        self.circle3 = None

        popisekPolomer = QLabel("Zadej poloměr",self)
        popisekPolomer.resize(100,25)
        popisekPolomer.move(25,275)

        linePolomer = QLineEdit(self)
        linePolomer.resize(100,25)
        linePolomer.move(10,300)

        popisekX = QLabel("Zadej hodnotu X", self)
        popisekX.resize(100,25)
        popisekX.move(20,350)

        lineX = QLineEdit(self)
        lineX.resize(100,25)
        lineX.move(10,375)

        popisekY = QLabel("Zadej hodnotu Y", self)
        popisekY.resize(100, 25)
        popisekY.move(20,425)

        lineY = QLineEdit(self)
        lineY.resize(100,25)
        lineY.move(10,450)

        buttonReset = QPushButton("Restartovat", self)
        buttonReset.clicked.connect(self.restart)
        buttonReset.resize(100, 50)
        buttonReset.move(650, 250)

    def draw_circle(self):
            self.circle = Ellipse(200, 200, 200, 200)
            self.update()

    def draw_circle2(self):
            self.circle2 = Ellipse(200, 200, 200, 200)
            self.update()

    def draw_circle3(self):
            self.circle3 = Ellipse(200,200,200,200)
            self.update()

    def restart(self):
            self.update()
            self.repaint()

    def paintEvent(self, event):
            QMainWindow.paintEvent(self, event)
            painter = QPainter(self)

            if not self.circle is None:
                pen = QPen(Qt.black, 5)
                painter.setPen(pen)
                painter.setBrush(Qt.red)
                painter.drawEllipse(self.circle.x, self.circle.y, self.circle.width, self.circle.height)
            if not self.circle2 is None:
                pen = QPen(Qt.black, 5)
                painter.setPen(pen)
                painter.setBrush(Qt.yellow)
                painter.drawEllipse(self.circle2.x, self.circle2.y, self.circle2.width, self.circle2.height)
            if not self.circle3 is None:
                pen = QPen(Qt.black, 5)
                painter.setPen(pen)
                painter.setBrush(Qt.green)
                painter.drawEllipse(self.circle3.x, self.circle3.y, self.circle3.width, self.circle3.height)




app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
sys.exit(app.exec_())
