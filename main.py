import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from UI import Ui_MainWindow

SCREEN_SIZE = [680, 480]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Супрематизм')

        self.figure = 'circle'
        self.size = random.randint(10, 100)
        self.color = QColor(255, 255, 0)
        self.coords = []
        self.flag = False

        self.pushButton = QPushButton('Добавить окружность', self)
        self.pushButton.clicked.connect(self.draw)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.pushButton)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def draw(self):
        self.size = random.randint(10, 100)
        self.x = random.randint(50, SCREEN_SIZE[0] - self.size)
        self.y = random.randint(50, SCREEN_SIZE[1] - self.size)

        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)
            qp.setPen(self.color)
            qp.setBrush(self.color)

            qp.drawEllipse(self.x, self.y, self.size, self.size)

            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec())
