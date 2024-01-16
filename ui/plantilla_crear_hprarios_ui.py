# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/plantilla_crear_hprarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout_2.addWidget(self.btn_guardar)
        self.bt_seleccion = QtWidgets.QPushButton(self.centralwidget)
        self.bt_seleccion.setStyleSheet("")
        self.bt_seleccion.setObjectName("bt_seleccion")
        self.horizontalLayout_2.addWidget(self.bt_seleccion)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bt_volver = QtWidgets.QPushButton(self.centralwidget)
        self.bt_volver.setObjectName("bt_volver")
        self.horizontalLayout_2.addWidget(self.bt_volver)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.ln_carrera = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_carrera.setReadOnly(True)
        self.ln_carrera.setObjectName("ln_carrera")
        self.horizontalLayout.addWidget(self.ln_carrera)
        self.btn_buscarCarr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscarCarr.setObjectName("btn_buscarCarr")
        self.horizontalLayout.addWidget(self.btn_buscarCarr)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.ln_nivel = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_nivel.setReadOnly(True)
        self.ln_nivel.setObjectName("ln_nivel")
        self.horizontalLayout.addWidget(self.ln_nivel)
        self.btn_buscarnivel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscarnivel.setObjectName("btn_buscarnivel")
        self.horizontalLayout.addWidget(self.btn_buscarnivel)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.ln_sesion = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_sesion.setObjectName("ln_sesion")
        self.horizontalLayout.addWidget(self.ln_sesion)
        self.btn_buscarSecc_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscarSecc_2.setObjectName("btn_buscarSecc_2")
        self.horizontalLayout.addWidget(self.btn_buscarSecc_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("3270 Nerd Font Mono")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(152, 228, 255);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_vistaPrevia = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vistaPrevia.setObjectName("btn_vistaPrevia")
        self.horizontalLayout_3.addWidget(self.btn_vistaPrevia)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar"))
        self.bt_seleccion.setText(_translate("MainWindow", "Activar Seleccion Multiple"))
        self.bt_volver.setText(_translate("MainWindow", "Volver"))
        self.label_2.setText(_translate("MainWindow", "Carrera"))
        self.btn_buscarCarr.setText(_translate("MainWindow", "buscar"))
        self.label_3.setText(_translate("MainWindow", "Nivel"))
        self.btn_buscarnivel.setText(_translate("MainWindow", "buscar"))
        self.label_4.setText(_translate("MainWindow", "Sesion"))
        self.btn_buscarSecc_2.setText(_translate("MainWindow", "buscar"))
        self.label.setText(_translate("MainWindow", "Nombre de la modalidad"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Horas"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lunes"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Martes"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Miercoles"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Jueves"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Viernes"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sabado"))
        self.btn_vistaPrevia.setText(_translate("MainWindow", "Vista Previa"))
