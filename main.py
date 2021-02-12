import sys
import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

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

    def getImage(self, ll, spn, l):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn},{spn}&l={l}"
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
