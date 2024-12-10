import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor

SCREEN_SIZE = [680, 480]


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Супрематизм')

        self.pushButton = QPushButton('Добавить окружность', self)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.pushButton)

        self.setLayout(layout)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.setCentralWidget(self.ui)

        self.resize(680, 480)

        self.size = random.randint(10, 100)
        self.coords = []
        self.flag = False

        self.ui.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.size = random.randint(10, 100)
        self.x = random.randint(50, SCREEN_SIZE[0] - self.size)
        self.y = random.randint(50, SCREEN_SIZE[1] - self.size)

        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

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
