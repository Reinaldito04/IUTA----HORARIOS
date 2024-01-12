# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/modalidad.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_salir_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_salir_2.setMinimumSize(QtCore.QSize(75, 31))
        self.bt_salir_2.setMaximumSize(QtCore.QSize(75, 31))
        self.bt_salir_2.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_salir_2.setObjectName("bt_salir_2")
        self.horizontalLayout.addWidget(self.bt_salir_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(171, 81))
        self.label_4.setMaximumSize(QtCore.QSize(171, 81))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/iutaImg.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bt_salir = QtWidgets.QPushButton(self.centralwidget)
        self.bt_salir.setMinimumSize(QtCore.QSize(75, 31))
        self.bt_salir.setMaximumSize(QtCore.QSize(75, 31))
        self.bt_salir.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_salir.setObjectName("bt_salir")
        self.horizontalLayout.addWidget(self.bt_salir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color:rgb(128, 179, 255);\n"
"border-radius:25px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.bt_aggView = QtWidgets.QPushButton(self.frame_2)
        self.bt_aggView.setMinimumSize(QtCore.QSize(161, 31))
        self.bt_aggView.setMaximumSize(QtCore.QSize(161, 31))
        self.bt_aggView.setStyleSheet("font-size:15px;\n"
"border:2px solid rgb(182, 255, 250);\n"
"border-radius:15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/adduser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_aggView.setIcon(icon)
        self.bt_aggView.setIconSize(QtCore.QSize(20, 20))
        self.bt_aggView.setObjectName("bt_aggView")
        self.verticalLayout_2.addWidget(self.bt_aggView)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.bt_deleteView = QtWidgets.QPushButton(self.frame_2)
        self.bt_deleteView.setMinimumSize(QtCore.QSize(161, 31))
        self.bt_deleteView.setMaximumSize(QtCore.QSize(161, 31))
        self.bt_deleteView.setStyleSheet("font-size:15px;\n"
"border:2px solid rgb(182, 255, 250);\n"
"border-radius:15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_deleteView.setIcon(icon1)
        self.bt_deleteView.setIconSize(QtCore.QSize(20, 20))
        self.bt_deleteView.setObjectName("bt_deleteView")
        self.verticalLayout_2.addWidget(self.bt_deleteView)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.bt_database = QtWidgets.QPushButton(self.frame_2)
        self.bt_database.setMinimumSize(QtCore.QSize(161, 31))
        self.bt_database.setMaximumSize(QtCore.QSize(161, 31))
        self.bt_database.setStyleSheet("font-size:15px;\n"
"border:2px solid rgb(182, 255, 250);\n"
"border-radius:15px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/users-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_database.setIcon(icon2)
        self.bt_database.setIconSize(QtCore.QSize(20, 20))
        self.bt_database.setObjectName("bt_database")
        self.verticalLayout_2.addWidget(self.bt_database)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_14.addWidget(self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_delete = QtWidgets.QWidget()
        self.page_delete.setObjectName("page_delete")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_delete)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.page_delete)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        spacerItem6 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.ln_busqueda = QtWidgets.QLineEdit(self.page_delete)
        self.ln_busqueda.setMinimumSize(QtCore.QSize(311, 31))
        self.ln_busqueda.setMaximumSize(QtCore.QSize(311, 31))
        self.ln_busqueda.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(128, 179, 255);")
        self.ln_busqueda.setObjectName("ln_busqueda")
        self.horizontalLayout_6.addWidget(self.ln_busqueda)
        spacerItem8 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.bt_search = QtWidgets.QPushButton(self.page_delete)
        self.bt_search.setStyleSheet("border:none;")
        self.bt_search.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_search.setIcon(icon3)
        self.bt_search.setIconSize(QtCore.QSize(20, 20))
        self.bt_search.setObjectName("bt_search")
        self.horizontalLayout_6.addWidget(self.bt_search)
        spacerItem9 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.label_10 = QtWidgets.QLabel(self.page_delete)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        spacerItem12 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.txt_name_3 = QtWidgets.QLineEdit(self.page_delete)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_name_3.sizePolicy().hasHeightForWidth())
        self.txt_name_3.setSizePolicy(sizePolicy)
        self.txt_name_3.setMinimumSize(QtCore.QSize(241, 30))
        self.txt_name_3.setMaximumSize(QtCore.QSize(241, 30))
        self.txt_name_3.setStyleSheet("font-size:18px;\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"border-radius:10px;")
        self.txt_name_3.setObjectName("txt_name_3")
        self.horizontalLayout_4.addWidget(self.txt_name_3)
        spacerItem13 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.label_11 = QtWidgets.QLabel(self.page_delete)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.txt_name_4 = QtWidgets.QLineEdit(self.page_delete)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_name_4.sizePolicy().hasHeightForWidth())
        self.txt_name_4.setSizePolicy(sizePolicy)
        self.txt_name_4.setMinimumSize(QtCore.QSize(241, 30))
        self.txt_name_4.setMaximumSize(QtCore.QSize(241, 30))
        self.txt_name_4.setStyleSheet("font-size:18px;\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"border-radius:10px;")
        self.txt_name_4.setObjectName("txt_name_4")
        self.horizontalLayout_3.addWidget(self.txt_name_4)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem17)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem18)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem19)
        self.bt_delete = QtWidgets.QPushButton(self.page_delete)
        self.bt_delete.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_delete.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_delete.setStyleSheet("QPushButton{border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0,0,0,0.5);\n"
"font-size:18px;\n"
"}")
        self.bt_delete.setObjectName("bt_delete")
        self.horizontalLayout_5.addWidget(self.bt_delete)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.page_delete)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem21)
        self.label_13 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem22)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 470))
        self.tableWidget.setStyleSheet("background-color:rgb(152, 228, 255);\n"
"font-size:15px;")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_6.addWidget(self.tableWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem23)
        self.bt_act = QtWidgets.QPushButton(self.page)
        self.bt_act.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_act.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_act.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_act.setIconSize(QtCore.QSize(20, 20))
        self.bt_act.setObjectName("bt_act")
        self.horizontalLayout_7.addWidget(self.bt_act)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.page)
        self.page_add = QtWidgets.QWidget()
        self.page_add.setObjectName("page_add")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.page_add)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.page_add)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem24)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.page_add)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_13.addWidget(self.label_2)
        spacerItem25 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem25)
        self.txt_Codigo = QtWidgets.QLineEdit(self.page_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_Codigo.sizePolicy().hasHeightForWidth())
        self.txt_Codigo.setSizePolicy(sizePolicy)
        self.txt_Codigo.setMinimumSize(QtCore.QSize(200, 31))
        self.txt_Codigo.setMaximumSize(QtCore.QSize(200, 31))
        self.txt_Codigo.setStyleSheet("font-size:18px;\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"border-radius:10px;")
        self.txt_Codigo.setObjectName("txt_Codigo")
        self.horizontalLayout_13.addWidget(self.txt_Codigo)
        self.verticalLayout_12.addLayout(self.horizontalLayout_13)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem26)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.page_add)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem27)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.txt_descripcion = QtWidgets.QLineEdit(self.page_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_descripcion.sizePolicy().hasHeightForWidth())
        self.txt_descripcion.setSizePolicy(sizePolicy)
        self.txt_descripcion.setMinimumSize(QtCore.QSize(200, 31))
        self.txt_descripcion.setMaximumSize(QtCore.QSize(200, 31))
        self.txt_descripcion.setStyleSheet("border:none;\n"
"border-bottom:2px solid white;\n"
"font-size:18px;\n"
"border-radius:10px;")
        self.txt_descripcion.setObjectName("txt_descripcion")
        self.horizontalLayout_10.addWidget(self.txt_descripcion)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem28)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.page_add)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        spacerItem29 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem29)
        self.txt_turno = QtWidgets.QLineEdit(self.page_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_turno.sizePolicy().hasHeightForWidth())
        self.txt_turno.setSizePolicy(sizePolicy)
        self.txt_turno.setMinimumSize(QtCore.QSize(200, 31))
        self.txt_turno.setMaximumSize(QtCore.QSize(200, 31))
        self.txt_turno.setStyleSheet("border:none;\n"
"border-bottom:2px solid white;\n"
"font-size:18px;\n"
"border-radius:10px;")
        self.txt_turno.setObjectName("txt_turno")
        self.horizontalLayout_12.addWidget(self.txt_turno)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem30)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.bt_clear = QtWidgets.QPushButton(self.page_add)
        self.bt_clear.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_clear.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_clear.setStyleSheet("QPushButton{border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0,0,0,0.5);\n"
"font-size:18px;\n"
"}")
        self.bt_clear.setObjectName("bt_clear")
        self.horizontalLayout_9.addWidget(self.bt_clear)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem31)
        self.bt_register = QtWidgets.QPushButton(self.page_add)
        self.bt_register.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_register.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_register.setStyleSheet("QPushButton{border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0,0,0,0.5);\n"
"font-size:18px;\n"
"}")
        self.bt_register.setObjectName("bt_register")
        self.horizontalLayout_9.addWidget(self.bt_register)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem32)
        self.horizontalLayout_16.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tablaHoras = QtWidgets.QTableWidget(self.page_add)
        self.tablaHoras.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tablaHoras.setObjectName("tablaHoras")
        self.tablaHoras.setColumnCount(1)
        self.tablaHoras.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHoras.setHorizontalHeaderItem(0, item)
        self.verticalLayout_8.addWidget(self.tablaHoras)
        self.label_8 = QtWidgets.QLabel(self.page_add)
        self.label_8.setStyleSheet("color:red;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.page_add)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.page_add)
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        self.label_7 = QtWidgets.QLabel(self.page_add)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.page_add)
        self.dateTimeEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.bt_aggHora = QtWidgets.QPushButton(self.page_add)
        self.bt_aggHora.setObjectName("bt_aggHora")
        self.verticalLayout_9.addWidget(self.bt_aggHora)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_13.addLayout(self.verticalLayout_8)
        self.horizontalLayout_16.addLayout(self.verticalLayout_13)
        self.stackedWidget.addWidget(self.page_add)
        self.horizontalLayout_14.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_salir_2.setText(_translate("MainWindow", "VOLVER"))
        self.bt_salir.setText(_translate("MainWindow", "SALIR"))
        self.bt_aggView.setText(_translate("MainWindow", "Agregar"))
        self.bt_deleteView.setText(_translate("MainWindow", "Eliminar"))
        self.bt_database.setText(_translate("MainWindow", "Registrados"))
        self.label_12.setText(_translate("MainWindow", "Eliminar Modalidad"))
        self.label_10.setText(_translate("MainWindow", "Turno"))
        self.label_11.setText(_translate("MainWindow", "Descripcion"))
        self.bt_delete.setText(_translate("MainWindow", "Eliminar"))
        self.label_13.setText(_translate("MainWindow", "Modalidad"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Modalidad"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Descripcion"))
        self.bt_act.setText(_translate("MainWindow", "Actualizar"))
        self.label.setText(_translate("MainWindow", "Registro de Modadlidad"))
        self.label_2.setText(_translate("MainWindow", "Codigo"))
        self.label_5.setText(_translate("MainWindow", "Descripcion"))
        self.label_3.setText(_translate("MainWindow", "Turno"))
        self.bt_clear.setText(_translate("MainWindow", "Limpiar"))
        self.bt_register.setText(_translate("MainWindow", "Registrar"))
        item = self.tablaHoras.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora"))
        self.label_8.setText(_translate("MainWindow", "POR FAVOR,AGREGAR LAS \n"
" HORAS  ORDEN"))
        self.label_6.setText(_translate("MainWindow", "Agregar modulos"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "h:mm AP"))
        self.label_7.setText(_translate("MainWindow", "A"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("MainWindow", "h:mm AP"))
        self.bt_aggHora.setText(_translate("MainWindow", "Agregar"))
