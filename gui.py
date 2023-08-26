from image_viewer import *
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.QtGui import QPixmap
import os
import sys
import Queries


class My_Application(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # self.ui.pushButtonSelec.clicked.connect(self.checkPath)
        self.ui.pushButtonGuardar.clicked.connect(self.guardar)

    def checkPath(self):
        image_path = self.ui.lineEditRuta.text()
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.ui.graphicsView.setScene(scene)

    def guardar(self):
        clave = self.ui.lineEditClave.text()
        ruta = self.ui.lineEditRuta.text()
        desc = self.ui.lineEditDesc.text()
        print(clave, ruta, desc)
        Queries.INSERT(clave=clave, file_path=ruta, descripcion=desc)
        Queries.SELECT("5")
        print("mostart")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_instance = My_Application()
    class_instance.show()
    sys.exit(app.exec_())