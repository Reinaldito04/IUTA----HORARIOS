# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\reybe\OneDrive\Escritorio\IUTA -- HORARIOS\ui\horarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 721, 611))
        self.frame.setStyleSheet("background-color:rgb(152, 228, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.bt_salir = QtWidgets.QPushButton(self.frame)
        self.bt_salir.setGeometry(QtCore.QRect(560, 30, 75, 31))
        self.bt_salir.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_salir.setObjectName("bt_salir")
        self.bt_close = QtWidgets.QPushButton(self.frame)
        self.bt_close.setGeometry(QtCore.QRect(40, 30, 101, 31))
        self.bt_close.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_close.setObjectName("bt_close")
        self.Loginboton = QtWidgets.QPushButton(self.frame)
        self.Loginboton.setGeometry(QtCore.QRect(80, 240, 171, 61))
        self.Loginboton.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\reybe\\OneDrive\\Escritorio\\IUTA -- HORARIOS\\ui\\imagenes/calendar3 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Loginboton.setIcon(icon)
        self.Loginboton.setIconSize(QtCore.QSize(20, 20))
        self.Loginboton.setObjectName("Loginboton")
        self.Loginboton_2 = QtWidgets.QPushButton(self.frame)
        self.Loginboton_2.setGeometry(QtCore.QRect(420, 240, 171, 61))
        self.Loginboton_2.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.Loginboton_2.setIcon(icon)
        self.Loginboton_2.setIconSize(QtCore.QSize(20, 20))
        self.Loginboton_2.setObjectName("Loginboton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HORARIOS"))
        self.bt_salir.setText(_translate("MainWindow", "SALIR"))
        self.bt_close.setText(_translate("MainWindow", "Volver"))
        self.Loginboton.setText(_translate("MainWindow", "Horarios Actuales"))
        self.Loginboton_2.setText(_translate("MainWindow", "Crear Horario"))
