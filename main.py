import sys
import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys, requests, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

SCREEN_SIZE = 600, 450


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

        self.radioButtonGroup.buttonClicked.connect(self.setView)
        self.l, self.spn, self.ll = 'map', '0.05', '37.677751,55.757718'

        self.PgUpButton.clicked.connect(self.up_scale)
        self.PgDownButton.clicked.connect(self.down_scale)
        self.scale = 10


    def initUI(self):
        self.setGeometry(50, 50, 620, 470)
        self.getImage()
        self.pixmap = QPixmap('map_file.png')
        self.image.setPixmap(self.pixmap)

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.ll}&z={self.scale}&spn={self.spn},{self.spn}&l={self.l}"
        self.response = requests.get(map_request)
        with open('map_file.png', "wb") as file:
            file.write(self.response.content)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            pass
        elif event.key() == Qt.Key_Down:
            pass
        elif event.key() == Qt.Key_Left:
            pass
        elif event.key() == Qt.Key_Right:
            pass

    def up_scale(self):
        if self.scale < 17:
            self.scale += 1

    def down_scale(self):
        if self.scale > 0:
            self.scale -= 1

    def setView(self, button):
        if button == self.radioButton1:
            self.l = 'map'
        if button == self.radioButton2:
            self.l = 'sat'
        if button == self.radioButton3:
            self.l = 'skl'
        os.remove('map_file.png')
        self.getImage()
        self.pixmap = QPixmap('map_file.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
