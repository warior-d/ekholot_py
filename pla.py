import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
from math import atan2, degrees, pi
import geopy
from geopy import Point
from geopy.distance import geodesic


def getCoord(grid, x_ground, y_ground, x_current, y_current):
    # https://github.com/geopy/geopy/blob/master/geopy/distance.py
    gridStep = Settings.GRID_STEP
    pixelLenght = grid / gridStep
    delta_x = x_current - x_ground
    delta_y = y_ground - y_current
    lengh_pixels = (((y_current - y_ground) ** (2)) + ((x_current - x_ground) ** (2))) ** (0.5)
    lengh_meters = lengh_pixels * pixelLenght
    rads = atan2(delta_y, -delta_x)
    rads %= 2 * pi
    degs = degrees(rads) - 90
    need_point = geodesic(kilometers=lengh_meters / 1000).destination(Point(Settings.LAT, Settings.LON), degs).format_decimal()
    return need_point

class Settings():
    GRID_STEP = 80
    FISHING_SIRCLE_RADIUS = 100
    FISHING_SIRCLE_QNT = 2
    MASHTAB_MIN = 1
    MASHTAB_MAX = 9
    RADIUS_EARTH_M = 6372795
    DEFAULT_MASHTAB = 4
    FILE_NAME = "OKA_19_0.jpg"
    LAT = 55.070145
    LON = 38.801207

class Label(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setFixedSize(220, 200)
        self.setPixmap(QPixmap(Settings.FILE_NAME)) #160

class Main(QWidget):
    mouse_old_pos = None
    label_old_pos = None
    old_pos = None
    mashtab = Settings.DEFAULT_MASHTAB
    grid_scale = ["10", "20", "40", "80", "160", "320", "640", "1000", "2000"]


    def __init__(self):
        super().__init__()
        #layout = QVBoxLayout()
        self.labelMap = Label(self)
        self.setGeometry(0, 0, 900, 800)
        self.labelMap.move(200, 150)
        #включим отслеживание мышки
        self.setMouseTracking(True)
        self.labelData = QLabel(self)
        self.labelData.resize(160, 10)
        self.labelData.move(10, 40)
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
        for i in range(0, 10000, Settings.GRID_STEP):
            painter.drawLine(x + i, 0, x + i, rec.height())
            painter.drawLine(x - i, 0, x - i, rec.height())

            painter.drawLine(0, y + i, rec.width(), y + i)
            painter.drawLine(0, y - i, rec.width(), y - i)
        painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_old_pos = event.pos() #позиция Мыши
            self.label_old_pos = self.labelMap.pos() #позиция Карты
            self.printer()
            print(getCoord(int(self.grid_scale[self.mashtab - 1]), self.labelMap.pos().x(), self.labelMap.pos().y(), self.mouse_old_pos.x(), self.mouse_old_pos.y()))

    def printer(self):
        print(122)

    def wheelEvent(self, event):
        if event.angleDelta().y()/120 > 0:
            if(self.mashtab < Settings.MASHTAB_MAX):
                self.mashtab = self.mashtab + 1
        else:
            if(self.mashtab > Settings.MASHTAB_MIN):
                self.mashtab = self.mashtab - 1
        currentGrid = self.grid_scale[self.mashtab - 1]
        self.labelData.setText('Mashtab | Grid: ( %s : %s m)' % (self.mashtab, currentGrid))

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("yep!!")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            #print(self.labelMap.pos())
            self.mouse_old_pos = None
            #print("mouseReleaseEvent:", self.mouse_old_pos)

    def mouseMoveEvent(self, event):
        # координаты self.labelMap.pos() - экранные пиксели
        # 80 px = 10m, 20m etc
        # latitude - (N,S) - широта - Y - увеличивается вверх
        # longitude - (E,W) - долгота - X - увеличивается направо
        if not self.mouse_old_pos:
            return
        delta = event.pos() - self.mouse_old_pos
        self.labelMap.move(self.label_old_pos + delta)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())