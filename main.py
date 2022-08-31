from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication([])
sz = QtWidgets.QWidget
mwindow = QtWidgets.QMainWindow

ui = uic.loadUi("main_window_design.ui")

def get_size_of_desktop():
    desktop = app.desktop()
    return (desktop.width(), desktop.height())

def get_size_of_win():
    return (app.desktop().screenGeometry().width(), app.desktop().screenGeometry().height())






print(get_size_of_desktop())

#print(wid)

ui.show()
app.exec()