import sys
import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

SCREEN_SIZE = 600, 450


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 620, 470)
        self.getImage()
        self.pixmap = QPixmap('map_file.png')
        self.image.setPixmap(self.pixmap)

    def getImage(self):
        map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.05,0.05&l=map"
        self.response = requests.get(map_request)
        with open('map_file.png', "wb") as file:
            file.write(self.response.content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
