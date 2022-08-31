import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen


class Label(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setFixedSize(220, 200)
        self.setPixmap(QPixmap("djerjinsky_karier.jpg"))

class Main(QWidget):
    mouse_old_pos = None
    label_old_pos = None
    old_pos = None
    mashtab = 1

    def __init__(self):
        super().__init__()
        #layout = QVBoxLayout()
        self.labelMap = Label(self)
        self.setGeometry(0, 0, 900, 800)
        self.labelMap.move(200, 150)
        #layout.addWidget(self.labelMap)
        #self.setLayout(layout)

    def paintEvent(self, event):
        rec = event.rect()
        if False:
            rec = QRect()
        x = self.labelMap.pos().x()
        y = self.labelMap.pos().y()
        painter = QPainter()
        painter.begin(self)
        for i in range(0, 10000, 80):
            painter.drawLine(x + i, 0, x + i, rec.height())
            painter.drawLine(x - i, 0, x - i, rec.height())

            painter.drawLine(0, y + i, rec.width(), y + i)
            painter.drawLine(0, y - i, rec.width(), y - i)
        painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_old_pos = event.pos()
            self.label_old_pos = self.labelMap.pos()
            self.printer()
            #print("Позиция мыши:", self.mouse_old_pos)
            #print("Позиция label:", self.label_old_pos)

    def printer(self):
        print(122)

    def wheelEvent(self, event):
        if event.angleDelta().y()/120 > 0:
            if(self.mashtab < 9):
                self.mashtab = self.mashtab + 1
        else:
            if(self.mashtab > 1):
                self.mashtab = self.mashtab - 1
        print(self.mashtab)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("yep!!")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            #print(self.labelMap.pos())
            self.mouse_old_pos = None
            #print("mouseReleaseEvent:", self.mouse_old_pos)

    def mouseMoveEvent(self, event):
        if not self.mouse_old_pos:
            return
        delta = event.pos() - self.mouse_old_pos
        self.labelMap.move(self.label_old_pos  + delta)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())