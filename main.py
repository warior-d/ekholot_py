import sys
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.openImageBtn = QPushButton('&Открыть изображение', self)
        self.saveImageBtn = QPushButton('&Сохранить изображение', self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.openImageBtn)
        layout.addWidget(self.saveImageBtn)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._itemImage = None

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.widget = Widget()
        self.widget.openImageBtn.clicked.connect(self.showOpenFileDialog)
#        self.saveImageBtn.clicked.connect(self.showSaveFileDialog)

        self._scene = QGraphicsScene()
        self.view = QGraphicsView(self._scene)
        self.showImage('im.png')
        self.view.setScene(self._scene)

        self.layout = QHBoxLayout(self.centralWidget)
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.widget)

    def showOpenFileDialog(self):
        file_name = QFileDialog.getOpenFileName(
                                self,
                                'Пожалуйста, выберите изображение',
                                '.',
                                'Image Files (*.png *.jpg *.jpeg *.bmp)'
                                               )[0]
        if not file_name:
            return
        if self._itemImage:
            # Удалить предыдущий элемент
            self._scene.removeItem(self._itemImage)
            del self._itemImage
        self.showImage(file_name)

    def showImage(self, file_name):
        self._itemImage = self._scene.addPixmap(QPixmap(file_name))
        self._itemImage.setFlag(QGraphicsItem.ItemIsMovable)            # <<<=====

    def closeEvent(self, event):
        """ Очистите все элементы в сцене, когда окно `закрыто` """
        self._scene.clear()
        self._itemImage = None
        super(MainWindow, self).closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.resize(QSize(700, 400))
    mw.show()
    sys.exit(app.exec_())