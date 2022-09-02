import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
from math import atan2, degrees, pi
import geopy
import os
from geopy import Point
from geopy.distance import geodesic, distance
import xml.etree.ElementTree as ET


def getCoordsFromKML(kmlfile):
    tree = ET.parse(kmlfile)
    root = tree.getroot()
    north = None
    west = None
    east = None
    south = None
    for elem in root[0]:
        for subelem in elem:
            if subelem.tag == 'north':
                north = subelem.text
            if subelem.tag == 'west':
                west = subelem.text
            if subelem.tag == 'east':
                east = subelem.text
            if subelem.tag == 'south':
                south = subelem.text
    coordinates = {'north': north, 'west': west, 'east': east, 'south': south}
    return coordinates


def getKMLfileName(picFile):
    PICfilename, PICfile_extension = picFile.split('.')
    KMLfile = None
    #TODO: scandir - сканирует текущую директорию!!!
    with os.scandir(os.getcwd()) as files:
        for file in files:
            if file.is_file():
                KMLfilename, KMLfile_extension = file.name.split('.')
                if (KMLfile_extension.upper() == "KML") and (KMLfilename.upper() == PICfilename.upper()):
                    KMLfile = KMLfilename + '.' + KMLfile_extension
    return KMLfile

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
    need_point = geodesic(kilometers=lengh_meters / 1000).destination(Point(Settings.LAT_NW, Settings.LON_NW), degs).format_decimal()
    return need_point

def distanceBetweenPointsMeters(lat1, lon1, lat2, lon2):
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)
    return geodesic(point1, point2).meters

class Settings():
    GRID_STEP = 80
    FISHING_SIRCLE_RADIUS = 100
    FISHING_SIRCLE_QNT = 2
    MASHTAB_MIN = 1
    MASHTAB_MAX = 9
    RADIUS_EARTH_M = 6372795
    DEFAULT_MASHTAB = 3
    FILE_NAME = "Lube.jpg" #"OKA_19_160.jpg"
    LAT_NW = None
    LON_NW = None
    LAT_SE = None
    LON_SE = None
    GRID_SCALE = ["10", "20", "40", "80", "160", "320", "640", "1000", "2000"]

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
    KMLfileName = getKMLfileName(Settings.FILE_NAME)


    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 900, 800)
        #layout = QVBoxLayout()
        self.labelMap = Label(self)
        self.labelMap.move(200, 150)
        #включим отслеживание мышки
        self.setMouseTracking(True)
        self.labelData = QLabel(self)
        self.labelData.resize(160, 10)
        self.labelData.move(10, 40)
        # Получим список координат
        coordinatesFromFile = getCoordsFromKML(getKMLfileName(Settings.FILE_NAME))
        Settings.LAT_NW, Settings.LON_NW, Settings.LAT_SE, Settings.LON_SE = coordinatesFromFile['north'], coordinatesFromFile['west'], coordinatesFromFile['south'], coordinatesFromFile['east']
        # Определим РЕАЛЬНОЕ (по координатам) расстояние между точками из KML
        real_distance_map = distanceBetweenPointsMeters(Settings.LAT_NW, Settings.LON_NW, Settings.LAT_SE, Settings.LON_SE)
        #print(real_distance_map)
        # Определим расстояние с учетом пикселей картинки и гридом!
        x1, y1 = self.labelMap.pos().x(), self.labelMap.pos().y()
        x2, y2 = x1 + self.labelMap.pixmap().width(), y1 + self.labelMap.pixmap().height()
        grid = int(Settings.GRID_SCALE[self.mashtab - 1])
        gridStep = Settings.GRID_STEP
        pixelLenght = grid / gridStep
        lengh_pixels = (((y2 - y1) ** (2)) + ((x2 - x1) ** (2))) ** (0.5)
        lengh_meters = lengh_pixels * pixelLenght
        #TODO: koef очень похож на DrDepth, округлять бы...
        koef = real_distance_map / lengh_meters
        # пересчитаем картинку и изменим ее
        width_new = self.labelMap.pixmap().width() * koef
        height_new = self.labelMap.pixmap().height() * koef
        # И отобразим на карте!
        self.rescaleMap(width_new, height_new)
        #layout.addWidget(self.labelMap)
        #self.setLayout(layout)


    def rescaleMap(self, width, height):
        self.labelMap.setPixmap(QPixmap(Settings.FILE_NAME).scaled(int(width), int(height)))
        print("rescale")

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
            print(getCoord(int(Settings.GRID_SCALE[self.mashtab - 1]), self.labelMap.pos().x(), self.labelMap.pos().y(), self.mouse_old_pos.x(), self.mouse_old_pos.y()))

    def wheelEvent(self, event):
        if event.angleDelta().y()/120 > 0:
            if(self.mashtab < Settings.MASHTAB_MAX):
                self.mashtab = self.mashtab + 1
        else:
            if(self.mashtab > Settings.MASHTAB_MIN):
                self.mashtab = self.mashtab - 1
        currentGrid = Settings.GRID_SCALE[self.mashtab - 1]
        self.labelData.setText('Mashtab | Grid: ( %s : %s m)' % (self.mashtab, currentGrid))

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("yep!!")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_old_pos = None

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