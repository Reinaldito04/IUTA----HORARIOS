# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\reybe\OneDrive\Escritorio\IUTA -- HORARIOS\ui\carreras.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 661, 581))
        self.frame.setStyleSheet("background-color:rgb(152, 228, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_salir = QtWidgets.QPushButton(self.frame)
        self.bt_salir.setGeometry(QtCore.QRect(560, 30, 75, 31))
        self.bt_salir.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_salir.setObjectName("bt_salir")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 181, 491))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.bt_agg = QtWidgets.QPushButton(self.frame_2)
        self.bt_agg.setGeometry(QtCore.QRect(20, 50, 141, 51))
        self.bt_agg.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_agg.setIconSize(QtCore.QSize(20, 20))
        self.bt_agg.setObjectName("bt_agg")
        self.bt_view = QtWidgets.QPushButton(self.frame_2)
        self.bt_view.setGeometry(QtCore.QRect(20, 210, 141, 51))
        self.bt_view.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_view.setIconSize(QtCore.QSize(20, 20))
        self.bt_view.setObjectName("bt_view")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 80, 441, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_agg = QtWidgets.QWidget()
        self.page_agg.setObjectName("page_agg")
        self.label_2 = QtWidgets.QLabel(self.page_agg)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.page_agg)
        self.label_5.setGeometry(QtCore.QRect(40, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size:15px;")
        self.label_5.setObjectName("label_5")
        self.txt_code = QtWidgets.QLineEdit(self.page_agg)
        self.txt_code.setGeometry(QtCore.QRect(190, 110, 191, 21))
        self.txt_code.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_code.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_code.setObjectName("txt_code")
        self.label_6 = QtWidgets.QLabel(self.page_agg)
        self.label_6.setGeometry(QtCore.QRect(40, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-size:15px;")
        self.label_6.setObjectName("label_6")
        self.txt_name = QtWidgets.QLineEdit(self.page_agg)
        self.txt_name.setGeometry(QtCore.QRect(190, 160, 191, 21))
        self.txt_name.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_name.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_name.setObjectName("txt_name")
        self.bt_agg_2 = QtWidgets.QPushButton(self.page_agg)
        self.bt_agg_2.setGeometry(QtCore.QRect(110, 220, 141, 41))
        self.bt_agg_2.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_agg_2.setIconSize(QtCore.QSize(20, 20))
        self.bt_agg_2.setObjectName("bt_agg_2")
        self.stackedWidget.addWidget(self.page_agg)
        self.page_edit = QtWidgets.QWidget()
        self.page_edit.setObjectName("page_edit")
        self.label_3 = QtWidgets.QLabel(self.page_edit)
        self.label_3.setGeometry(QtCore.QRect(60, 40, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.ln_busqueda = QtWidgets.QLineEdit(self.page_edit)
        self.ln_busqueda.setGeometry(QtCore.QRect(30, 80, 311, 21))
        self.ln_busqueda.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(128, 179, 255);")
        self.ln_busqueda.setObjectName("ln_busqueda")
        self.bt_search = QtWidgets.QPushButton(self.page_edit)
        self.bt_search.setGeometry(QtCore.QRect(340, 80, 75, 21))
        self.bt_search.setStyleSheet("border:none;")
        self.bt_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\reybe\\OneDrive\\Escritorio\\IUTA -- HORARIOS\\ui\\imagenes/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_search.setIcon(icon)
        self.bt_search.setIconSize(QtCore.QSize(20, 20))
        self.bt_search.setObjectName("bt_search")
        self.txt_name_2 = QtWidgets.QLineEdit(self.page_edit)
        self.txt_name_2.setGeometry(QtCore.QRect(180, 150, 191, 21))
        self.txt_name_2.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_name_2.setObjectName("txt_name_2")
        self.txt_cedula_2 = QtWidgets.QLineEdit(self.page_edit)
        self.txt_cedula_2.setGeometry(QtCore.QRect(180, 250, 191, 21))
        self.txt_cedula_2.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_cedula_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_cedula_2.setObjectName("txt_cedula_2")
        self.txt_apell_2 = QtWidgets.QLineEdit(self.page_edit)
        self.txt_apell_2.setGeometry(QtCore.QRect(180, 200, 191, 21))
        self.txt_apell_2.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_apell_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_apell_2.setObjectName("txt_apell_2")
        self.label_8 = QtWidgets.QLabel(self.page_edit)
        self.label_8.setGeometry(QtCore.QRect(30, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font-size:15px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_edit)
        self.label_9.setGeometry(QtCore.QRect(30, 150, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-size:15px;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_edit)
        self.label_10.setGeometry(QtCore.QRect(30, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-size:15px;")
        self.label_10.setObjectName("label_10")
        self.bt_edit_2 = QtWidgets.QPushButton(self.page_edit)
        self.bt_edit_2.setGeometry(QtCore.QRect(30, 340, 91, 41))
        self.bt_edit_2.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_edit_2.setIconSize(QtCore.QSize(20, 20))
        self.bt_edit_2.setObjectName("bt_edit_2")
        self.bt_clear = QtWidgets.QPushButton(self.page_edit)
        self.bt_clear.setGeometry(QtCore.QRect(300, 340, 111, 41))
        self.bt_clear.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_clear.setIconSize(QtCore.QSize(20, 20))
        self.bt_clear.setObjectName("bt_clear")
        self.bt_delete = QtWidgets.QPushButton(self.page_edit)
        self.bt_delete.setGeometry(QtCore.QRect(170, 340, 101, 41))
        self.bt_delete.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_delete.setIconSize(QtCore.QSize(20, 20))
        self.bt_delete.setObjectName("bt_delete")
        self.stackedWidget.addWidget(self.page_edit)
        self.page_view = QtWidgets.QWidget()
        self.page_view.setObjectName("page_view")
        self.label_4 = QtWidgets.QLabel(self.page_view)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.bt_act = QtWidgets.QPushButton(self.page_view)
        self.bt_act.setGeometry(QtCore.QRect(260, 350, 141, 51))
        self.bt_act.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_act.setIconSize(QtCore.QSize(20, 20))
        self.bt_act.setObjectName("bt_act")
        self.tableWidget = QtWidgets.QTableWidget(self.page_view)
        self.tableWidget.setGeometry(QtCore.QRect(100, 80, 201, 241))
        self.tableWidget.setStyleSheet("background-color:rgb(152, 228, 255);\n"
"font-size:14px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.stackedWidget.addWidget(self.page_view)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.bt_back = QtWidgets.QPushButton(self.frame)
        self.bt_back.setGeometry(QtCore.QRect(50, 30, 101, 31))
        self.bt_back.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_back.setObjectName("bt_back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_salir.setText(_translate("MainWindow", "SALIR"))
        self.bt_agg.setText(_translate("MainWindow", "Agregar "))
        self.bt_view.setText(_translate("MainWindow", "Visualizar"))
        self.label_2.setText(_translate("MainWindow", "AGREGAR"))
        self.label_5.setText(_translate("MainWindow", "Codigo"))
        self.label_6.setText(_translate("MainWindow", "Nombre"))
        self.bt_agg_2.setText(_translate("MainWindow", "Agregar "))
        self.label_3.setText(_translate("MainWindow", "EDITAR"))
        self.label_8.setText(_translate("MainWindow", "C.I"))
        self.label_9.setText(_translate("MainWindow", "Nombres"))
        self.label_10.setText(_translate("MainWindow", "Apellidos"))
        self.bt_edit_2.setText(_translate("MainWindow", "Modificar"))
        self.bt_clear.setText(_translate("MainWindow", "Limpiar"))
        self.bt_delete.setText(_translate("MainWindow", "Eliminar"))
        self.label_4.setText(_translate("MainWindow", "VISUALIZAR"))
        self.bt_act.setText(_translate("MainWindow", "Actualizar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descripción"))
        self.label.setText(_translate("MainWindow", "CARRERAS"))
        self.bt_back.setText(_translate("MainWindow", "Volver"))