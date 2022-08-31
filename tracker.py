# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 650)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.LayDisplays = QtWidgets.QHBoxLayout()
        self.LayDisplays.setObjectName("LayDisplays")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_7.addWidget(self.lcdNumber)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_7.addWidget(self.lcdNumber_2)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_7.addWidget(self.lcdNumber_3)
        self.LayDisplays.addLayout(self.verticalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LayDisplays.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.LayDisplays)
        self.LaySliders = QtWidgets.QHBoxLayout()
        self.LaySliders.setObjectName("LaySliders")
        self.Prozrach = QtWidgets.QSlider(self.centralwidget)
        self.Prozrach.setMinimum(1)
        self.Prozrach.setMaximum(10)
        self.Prozrach.setPageStep(1)
        self.Prozrach.setSliderPosition(1)
        self.Prozrach.setOrientation(QtCore.Qt.Vertical)
        self.Prozrach.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Prozrach.setTickInterval(1)
        self.Prozrach.setObjectName("Prozrach")
        self.LaySliders.addWidget(self.Prozrach)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LaySliders.addItem(spacerItem1)
        self.Mashtab = QtWidgets.QSlider(self.centralwidget)
        self.Mashtab.setMinimum(1)
        self.Mashtab.setMaximum(10)
        self.Mashtab.setPageStep(1)
        self.Mashtab.setOrientation(QtCore.Qt.Vertical)
        self.Mashtab.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Mashtab.setTickInterval(1)
        self.Mashtab.setObjectName("Mashtab")
        self.LaySliders.addWidget(self.Mashtab)
        self.verticalLayout_8.addLayout(self.LaySliders)
        self.LayButtons = QtWidgets.QHBoxLayout()
        self.LayButtons.setObjectName("LayButtons")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LayButtons.addItem(spacerItem2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.LayButtons.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.LayButtons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSettings = QtWidgets.QMenu(self.menuTools)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionShut_Down = QtWidgets.QAction(MainWindow)
        self.actionShut_Down.setObjectName("actionShut_Down")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNMEA_Connection = QtWidgets.QAction(MainWindow)
        self.actionNMEA_Connection.setObjectName("actionNMEA_Connection")
        self.actionNMEA_Connection_2 = QtWidgets.QAction(MainWindow)
        self.actionNMEA_Connection_2.setObjectName("actionNMEA_Connection_2")
        self.actionBackgroung = QtWidgets.QAction(MainWindow)
        self.actionBackgroung.setObjectName("actionBackgroung")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionShut_Down)
        self.menuSettings.addAction(self.actionNMEA_Connection_2)
        self.menuTools.addAction(self.menuSettings.menuAction())
        self.menuTools.addAction(self.actionBackgroung)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pandion"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionShut_Down.setText(_translate("MainWindow", "Shut Down"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNMEA_Connection.setText(_translate("MainWindow", "NMEA/Connection"))
        self.actionNMEA_Connection_2.setText(_translate("MainWindow", "NMEA/Connection"))
        self.actionBackgroung.setText(_translate("MainWindow", "Backgroung"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
