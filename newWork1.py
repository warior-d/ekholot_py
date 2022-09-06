import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
import csv
import random
import matplotlib.pyplot as plt
from geopy import Point
from geopy.distance import geodesic, distance
import math, numpy as np

class Settings():
    GRID_STEP = 80
    NEED_GRID = 0
    FISHING_SIRCLE_RADIUS = 100
    FISHING_SIRCLE_QNT = 2
    MASHTAB_MIN = 1
    MASHTAB_MAX = 9
    RADIUS_EARTH_M = 6372795
    FILE_NAME = "dzerj.jpg" #"OKA_19_160.jpg"
    FILE_DEPTH_NAME = "djer.csv"  # "OKA_19_160.jpg"
    LAT_NW = None
    LON_NW = None
    LAT_SE = None
    LON_SE = None
    DEFAULT_MASHTAB = 5
    GRID_SCALE = ["10", "20", "40", "80", "160", "320", "640", "1000", "2000"]
    #               1     2     3     4     5      6      7       8       9

class Main(QWidget):
    mouse_old_pos = None
    label_old_pos = None
    old_pos = None
    mashtab = Settings.DEFAULT_MASHTAB
    startLat = None
    startLon = None
    startPixX = None
    startPixY = None
    array = []


    def __init__(self):
        super().__init__()
        self.setGeometry(0, 20, 1200, 800)
        self.depthParsing()
        self.startPixX = self.width()/2
        self.startPixY = self.height()/2

    def depthParsing(self):
        with open(Settings.FILE_DEPTH_NAME) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                a = row[0]
                b = row[1]
                c = row[2]
                curArr = [a, b, c]
                self.array.append(curArr)
                line_count = line_count + 1
        #print(self.array)



    def getCoord(self, lat_base, lon_base, lat_current, lon_current, baseX, baseY):
        point1 = (lat_base, lon_base)
        point2 = (lat_current, lon_current)
        real_dist = geodesic(point1, point2).meters
        grid = int(Settings.GRID_SCALE[self.mashtab - 1])
        gridStep = Settings.GRID_STEP
        pixelLenght = grid / gridStep  #40m/80px = 0.5m in pixel
        real_dist_in_pixels = real_dist / pixelLenght
        dLon = float(lon_current) - float(lon_base)
        y = math.sin(dLon) * math.cos(lat_current)
        x = math.cos(float(lat_base)) * math.sin(float(lat_current)) - math.sin(float(lat_base)) * math.cos(float(lat_current)) * math.cos(dLon)
        rads = math.atan2(y, x)
        rads %= 2 * math.pi
        degsa = 90 - math.degrees(rads)
        if degsa < 0:
            degsa+=360
        degrees = degsa * math.pi / 180
        relX = baseX + (real_dist_in_pixels * math.cos(degrees))
        relY = baseY - (real_dist_in_pixels * math.sin(degrees)) # 0 & 180
        #print('coord1: {} coord2: {} degsa: {} real_dist_in_pixels: {} relX: {} relY: {}'.format(point1, point2, degsa, real_dist, real_dist_in_pixels, relX, relY))
        point = (int(relX), int(relY))
        return point

    def paintEvent(self, paint_event):
        painter = QPainter()
        painter.begin(self)
        self.drawPoints(painter)
        painter.end()

    def drawPoints(self, painter):
        pen = QPen()
        pen.setWidth(5)
        k = 0
        for i in self.array:
            dep = float(i[2])
            x = float(i[0])
            y = float(i[1])
            pen.setColor(QColor(self.getColor(dep)))
            painter.setPen(pen)
            if k == 0:
                self.startLat = x
                self.startLon = y
                #painter.drawPoint(int(self.width()/2), int(self.height()/2))
                #print(self.width()/2, self.height()/2)
            else:
                relX, relY = self.getCoord(self.startLat, self.startLon, x, y, 900, 200)
                painter.drawPoint(int(relX), int(relY))
            k = k + 1


    def getColor(self, depth):
        color = None
        if 0 <= depth <= 0.75:
            color = '#990000'
        if 0.75 < depth <= 1.5:
            color = '#cc0000'
        if 1.5 < depth <= 2.25:
            color = '#ff0000'
        if 2.25 < depth <= 3:
            color = '#ff3300'
        if 3 < depth <= 3.75:
            color = '#ff6600'
        if 3.75 < depth <= 4.5:
            color = '#ff9900'
        if 4.5 < depth <= 5.25:
            color = '#ffcc00'
        if 5.25 < depth <= 6:
            color = '#ffff00'
        if 6 < depth <= 6.75:
            color = '#ccff33'
        if 6.75 < depth <= 7.5:
            color = '#99ff66'
        if 7.5 < depth <= 8.25:
            color = '#66ff99'
        if 8.25 < depth <= 9:
            color = '#33ffcc'
        if 9 < depth <= 9.75:
            color = '#00ffff'
        if 9.75 < depth <= 10.5:
            color = '#00ccff'
        if 10.5 < depth <= 11.25:
            color = '#0099ff'
        if 11.25 < depth <= 12:
            color = '#0066ff'
        if 12 < depth <= 12.75:
            color = '#0033ff'
        if 12.75 < depth <= 13.5:
            color = '#0000ff'
        if 13.5 < depth <= 14.25:
            color = '#0000cc'
        if 14.25 < depth:
            color = '#000099'
        return color




    def showDepths(self):
        fileDepth = Settings.FILE_DEPTH_NAME


    def keyPressEvent(self, event):
        click = event.key()
        if click == Qt.Key_Space:
            if Settings.NEED_GRID == 0:
                Settings.NEED_GRID = 1
                self.update()
            else:
                Settings.NEED_GRID = 0
                self.update()
        if click == Qt.Key_Q:
            self.depthParsing()





if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())