import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Label(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(220, 200)
        self.setPixmap(QPixmap("osm_logo.svg"))
'''
    def mousePressEvent(self, event):
        print("Внутри label:", event.pos())
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return

        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)
'''

class Main(QWidget):
    mouse_old_pos = None
    label_old_pos = None
    old_pos = None

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = Label(self)
        self.setGeometry(100, 60, 1000, 800)
        self.label.move(100, 150)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_old_pos = event.pos()
            self.label_old_pos = self.label.pos()
            print("Позиция мыши:", self.mouse_old_pos)
            print("Позиция label:", self.label_old_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_old_pos = None
            print("mouseReleaseEvent:", self.mouse_old_pos)

    def mouseMoveEvent(self, event):
        if not self.mouse_old_pos:
            return

        delta = event.pos() - self.mouse_old_pos
        delta_label = event.pos() - self.label_old_pos
        self.label.move(self.label_old_pos  + delta)  ##self.label.pos()
        print("delta window:", delta)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())