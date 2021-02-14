import sys
import requests
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys, requests, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

SCREEN_SIZE = 600, 450


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setGeometry(50, 50, 620, 470)
        self.l, self.spn, self.ll, self.scale = 'map', '0.05', '37.677751,55.757718', 10
        self.radioButtonGroup.buttonClicked.connect(self.setView)
        self.PgUpButton.clicked.connect(self.up_scale)
        self.PgDownButton.clicked.connect(self.down_scale)
        self.getImage()
        self.pixmap = QPixmap('map_file.png')
        self.image.setPixmap(self.pixmap)

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.ll}&z={self.scale}&spn={self.spn},{self.spn}&l={self.l}"
        self.response = requests.get(map_request)
        with open('map_file.png', "wb") as file:
            file.write(self.response.content)

    def keyPressEvent(self, event):
        self.y, self.x = [float(x) for x in self.ll.split(',')]
        if event.key() == Qt.Key_Up:
            self.x += float(self.spn) * 2
        elif event.key() == Qt.Key_Down:
            self.x -= float(self.spn) * 2
        elif event.key() == Qt.Key_Left:
            self.y -= float(self.spn) * 2
        elif event.key() == Qt.Key_Right:
            self.y += float(self.spn) * 2
        self.ll = f'{str(self.y)},{str(self.x)}'
        self.getImage()
        self.pixmap = QPixmap('map_file.png')
        self.image.setPixmap(self.pixmap)

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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
