# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/plantilla_menu_de_horarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_back = QtWidgets.QPushButton(self.centralwidget)
        self.bt_back.setObjectName("bt_back")
        self.horizontalLayout.addWidget(self.bt_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bt_salir = QtWidgets.QPushButton(self.centralwidget)
        self.bt_salir.setObjectName("bt_salir")
        self.horizontalLayout.addWidget(self.bt_salir)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 731, 386))
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_55 = QtWidgets.QLabel(self.page)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_5.addWidget(self.label_55)
        self.ln_disponibilidad_aula = QtWidgets.QLineEdit(self.page)
        self.ln_disponibilidad_aula.setReadOnly(True)
        self.ln_disponibilidad_aula.setObjectName("ln_disponibilidad_aula")
        self.horizontalLayout_5.addWidget(self.ln_disponibilidad_aula)
        self.bt_buscar = QtWidgets.QPushButton(self.page)
        self.bt_buscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/baseline-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_buscar.setIcon(icon)
        self.bt_buscar.setObjectName("bt_buscar")
        self.horizontalLayout_5.addWidget(self.bt_buscar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/university.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 731, 386))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.label_57 = QtWidgets.QLabel(self.page_2)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_11.addWidget(self.label_57)
        self.ln_disponibilidad_profesores = QtWidgets.QLineEdit(self.page_2)
        self.ln_disponibilidad_profesores.setReadOnly(True)
        self.ln_disponibilidad_profesores.setObjectName("ln_disponibilidad_profesores")
        self.horizontalLayout_11.addWidget(self.ln_disponibilidad_profesores)
        self.bt_profesor = QtWidgets.QPushButton(self.page_2)
        self.bt_profesor.setText("")
        self.bt_profesor.setIcon(icon)
        self.bt_profesor.setObjectName("bt_profesor")
        self.horizontalLayout_11.addWidget(self.bt_profesor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/adduser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 731, 386))
        self.page_3.setObjectName("page_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_73 = QtWidgets.QLabel(self.page_3)
        self.label_73.setObjectName("label_73")
        self.horizontalLayout_20.addWidget(self.label_73)
        self.ln_disponibilidad_carrera = QtWidgets.QLineEdit(self.page_3)
        self.ln_disponibilidad_carrera.setReadOnly(True)
        self.ln_disponibilidad_carrera.setObjectName("ln_disponibilidad_carrera")
        self.horizontalLayout_20.addWidget(self.ln_disponibilidad_carrera)
        self.bt_carrerabuscar = QtWidgets.QPushButton(self.page_3)
        self.bt_carrerabuscar.setText("")
        self.bt_carrerabuscar.setIcon(icon)
        self.bt_carrerabuscar.setObjectName("bt_carrerabuscar")
        self.horizontalLayout_20.addWidget(self.bt_carrerabuscar)
        self.ln_disponibilidad_seccion = QtWidgets.QLineEdit(self.page_3)
        self.ln_disponibilidad_seccion.setReadOnly(True)
        self.ln_disponibilidad_seccion.setObjectName("ln_disponibilidad_seccion")
        self.horizontalLayout_20.addWidget(self.ln_disponibilidad_seccion)
        self.bt_seccionbuscar = QtWidgets.QPushButton(self.page_3)
        self.bt_seccionbuscar.setText("")
        self.bt_seccionbuscar.setIcon(icon)
        self.bt_seccionbuscar.setObjectName("bt_seccionbuscar")
        self.horizontalLayout_20.addWidget(self.bt_seccionbuscar)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_20)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/users-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_3, icon3, "")
        self.verticalLayout_5.addWidget(self.toolBox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.bt_crear = QtWidgets.QPushButton(self.centralwidget)
        self.bt_crear.setMinimumSize(QtCore.QSize(160, 61))
        self.bt_crear.setMaximumSize(QtCore.QSize(160, 61))
        self.bt_crear.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/calendar3 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_crear.setIcon(icon4)
        self.bt_crear.setIconSize(QtCore.QSize(20, 20))
        self.bt_crear.setObjectName("bt_crear")
        self.horizontalLayout_2.addWidget(self.bt_crear)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_back.setText(_translate("MainWindow", "Volver "))
        self.label.setText(_translate("MainWindow", "nombre de la modalidad"))
        self.bt_salir.setText(_translate("MainWindow", "Volver al menu Principal"))
        self.label_55.setText(_translate("MainWindow", "Verificar disponibilidad"))
        self.ln_disponibilidad_aula.setPlaceholderText(_translate("MainWindow", "Aula"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Disponibilidad Aulas"))
        self.label_57.setText(_translate("MainWindow", "Verificar disponibilidad"))
        self.ln_disponibilidad_profesores.setPlaceholderText(_translate("MainWindow", "Profesor"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Disponibilidad Profesores"))
        self.label_73.setText(_translate("MainWindow", "Verificar disponibilidad"))
        self.ln_disponibilidad_carrera.setPlaceholderText(_translate("MainWindow", "Carrera"))
        self.ln_disponibilidad_seccion.setPlaceholderText(_translate("MainWindow", "Seccion"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Disponibilidad Seccion"))
        self.bt_crear.setText(_translate("MainWindow", "Ver y Crear Horario"))
