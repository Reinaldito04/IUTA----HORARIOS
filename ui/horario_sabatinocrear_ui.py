# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/horario_sabatinocrear.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 767)
        MainWindow.setStyleSheet("background-color:rgb(152, 228, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_volver = QtWidgets.QPushButton(self.centralwidget)
        self.bt_volver.setObjectName("bt_volver")
        self.horizontalLayout_3.addWidget(self.bt_volver)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.ln_carrera = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_carrera.setObjectName("ln_carrera")
        self.horizontalLayout.addWidget(self.ln_carrera)
        self.btn_buscarCarr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscarCarr.setObjectName("btn_buscarCarr")
        self.horizontalLayout.addWidget(self.btn_buscarCarr)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.ln_sesion = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_sesion.setObjectName("ln_sesion")
        self.horizontalLayout.addWidget(self.ln_sesion)
        self.btn_buscarSecc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscarSecc.setObjectName("btn_buscarSecc")
        self.horizontalLayout.addWidget(self.btn_buscarSecc)
        self.lineEdit_Periodo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Periodo.setObjectName("lineEdit_Periodo")
        self.horizontalLayout.addWidget(self.lineEdit_Periodo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(550)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout_2.addWidget(self.btn_guardar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_vistaPrevia = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vistaPrevia.setObjectName("btn_vistaPrevia")
        self.horizontalLayout_2.addWidget(self.btn_vistaPrevia)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_volver.setText(_translate("MainWindow", "Volver"))
        self.label.setText(_translate("MainWindow", "Horario Sabatino"))
        self.label_2.setText(_translate("MainWindow", "Carrera"))
        self.btn_buscarCarr.setText(_translate("MainWindow", "buscar"))
        self.label_3.setText(_translate("MainWindow", "Seccion"))
        self.btn_buscarSecc.setText(_translate("MainWindow", "buscar"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "07:30 A 08:10"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "08:10 A 08:50"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "08:50 A 09:30"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "09:30 A 10:10"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "10:10 A 10:50"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "10:50 A 11:30"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "11:30 A 12:10"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "12:10 A 12:50"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "12:50 A 01:30"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "01:30 A 02:10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "02:10 A 02:50"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "02:50 A 03:30"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "03:30 A 04:10"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "04:10 A 04:50"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "04:50 A 05:30"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sabado"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar"))
        self.btn_vistaPrevia.setText(_translate("MainWindow", "Vista Previa"))