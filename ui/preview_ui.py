# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/preview.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(466, 462)
        Dialog.setStyleSheet("background-color:rgb(152, 228, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size:14px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.foto = QtWidgets.QLabel(Dialog)
        self.foto.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.foto.setScaledContents(True)
        self.foto.setObjectName("foto")
        self.verticalLayout.addWidget(self.foto)
        self.btn_siguiente = QtWidgets.QPushButton(Dialog)
        self.btn_siguiente.setObjectName("btn_siguiente")
        self.verticalLayout.addWidget(self.btn_siguiente)
        self.btn_anterior = QtWidgets.QPushButton(Dialog)
        self.btn_anterior.setObjectName("btn_anterior")
        self.verticalLayout.addWidget(self.btn_anterior)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Vista Previa"))
        self.foto.setText(_translate("Dialog", "Foto"))
        self.btn_siguiente.setText(_translate("Dialog", "Siguiente"))
        self.btn_anterior.setText(_translate("Dialog", "Anterior"))
