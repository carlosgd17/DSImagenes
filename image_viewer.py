from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(766, 569)

        """titulo insertar"""
        self.labelIns = QtWidgets.QLabel(Dialog)
        self.labelIns.setGeometry(QtCore.QRect(380, 15, 125, 20))
        self.labelIns.setObjectName("labelIns")

        # etiqueta y textbox clave
        self.labelClave = QtWidgets.QLabel(Dialog)
        self.labelClave.setGeometry(QtCore.QRect(30, 40, 125, 30))
        self.labelClave.setObjectName("labelClave")

        self.lineEditClave= QtWidgets.QLineEdit(Dialog)
        self.lineEditClave.setGeometry(QtCore.QRect(170, 40, 550, 30))
        self.lineEditClave.setObjectName("lineEditRuta")

        # etiqueta y textbox Ruta
        self.labelRuta = QtWidgets.QLabel(Dialog)
        self.labelRuta.setGeometry(QtCore.QRect(30, 80, 125, 30))
        self.labelRuta.setObjectName("labelRuta")

        self.lineEditRuta = QtWidgets.QLineEdit(Dialog)
        self.lineEditRuta.setGeometry(QtCore.QRect(170, 80, 550, 30))
        self.lineEditRuta.setObjectName("lineEditRuta")

        # etiqueta y textbox Descripcion
        self.labelDesc = QtWidgets.QLabel(Dialog)
        self.labelDesc.setGeometry(QtCore.QRect(30, 120, 125, 30))
        self.labelDesc.setObjectName("labelDesc")

        self.lineEditDesc = QtWidgets.QLineEdit(Dialog)
        self.lineEditDesc.setGeometry(QtCore.QRect(170, 120, 550, 30))
        self.lineEditDesc.setObjectName("lineEditDesc")

        # boton guardar
        self.pushButtonGuardar = QtWidgets.QPushButton(Dialog)
        self.pushButtonGuardar.setGeometry(QtCore.QRect(370, 160, 75, 30))
        self.pushButtonGuardar.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Imagenes"))

        self.labelIns.setText(_translate("Dialog", "Insertar"))
        self.labelClave.setText(_translate("Dialog", "Clave:"))
        self.labelRuta.setText(_translate("Dialog", "Ruta de la imagen:"))
        self.labelDesc.setText(_translate("Dialog", "Descripcion:"))
        self.pushButtonGuardar.setText(_translate("Dialog", "Guardar"))