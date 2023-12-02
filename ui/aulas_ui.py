# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/aulas.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 661)
        MainWindow.setStyleSheet("background-color:rgb(152, 228, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.bt_aggView_2 = QtWidgets.QPushButton(self.frame_2)
        self.bt_aggView_2.setMinimumSize(QtCore.QSize(161, 31))
        self.bt_aggView_2.setMaximumSize(QtCore.QSize(161, 31))
        self.bt_aggView_2.setStyleSheet("font-size:15px;\n"
"border:2px solid rgb(182, 255, 250);\n"
"border-radius:15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/adduser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_aggView_2.setIcon(icon)
        self.bt_aggView_2.setIconSize(QtCore.QSize(20, 20))
        self.bt_aggView_2.setObjectName("bt_aggView_2")
        self.verticalLayout_2.addWidget(self.bt_aggView_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.bt_sedes = QtWidgets.QPushButton(self.frame_2)
        self.bt_sedes.setMinimumSize(QtCore.QSize(161, 31))
        self.bt_sedes.setMaximumSize(QtCore.QSize(161, 31))
        self.bt_sedes.setStyleSheet("font-size:15px;\n"
"border:2px solid rgb(182, 255, 250);\n"
"border-radius:15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/university.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_sedes.setIcon(icon1)
        self.bt_sedes.setIconSize(QtCore.QSize(20, 20))
        self.bt_sedes.setObjectName("bt_sedes")
        self.verticalLayout_2.addWidget(self.bt_sedes)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.bt_deleteView = QtWidgets.QPushButton(self.frame_2)
        self.bt_deleteView.setMinimumSize(QtCore.QSize(161, 31))
        self.bt_deleteView.setMaximumSize(QtCore.QSize(161, 31))
        self.bt_deleteView.setStyleSheet("font-size:15px;\n"
"border:2px solid rgb(182, 255, 250);\n"
"border-radius:15px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_deleteView.setIcon(icon2)
        self.bt_deleteView.setIconSize(QtCore.QSize(20, 20))
        self.bt_deleteView.setObjectName("bt_deleteView")
        self.verticalLayout_2.addWidget(self.bt_deleteView)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.bt_database = QtWidgets.QPushButton(self.frame_2)
        self.bt_database.setMinimumSize(QtCore.QSize(161, 31))
        self.bt_database.setMaximumSize(QtCore.QSize(161, 31))
        self.bt_database.setStyleSheet("font-size:15px;\n"
"border:2px solid rgb(182, 255, 250);\n"
"border-radius:15px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/users-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_database.setIcon(icon3)
        self.bt_database.setIconSize(QtCore.QSize(20, 20))
        self.bt_database.setObjectName("bt_database")
        self.verticalLayout_2.addWidget(self.bt_database)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.ln_busqueda = QtWidgets.QLineEdit(self.page_delete)
        self.ln_busqueda.setMinimumSize(QtCore.QSize(311, 31))
        self.ln_busqueda.setMaximumSize(QtCore.QSize(311, 31))
        self.ln_busqueda.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(128, 179, 255);")
        self.ln_busqueda.setObjectName("ln_busqueda")
        self.horizontalLayout_6.addWidget(self.ln_busqueda)
        spacerItem7 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.bt_search = QtWidgets.QPushButton(self.page_delete)
        self.bt_search.setStyleSheet("border:none;")
        self.bt_search.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_search.setIcon(icon4)
        self.bt_search.setIconSize(QtCore.QSize(20, 20))
        self.bt_search.setObjectName("bt_search")
        self.horizontalLayout_6.addWidget(self.bt_search)
        spacerItem8 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
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
        spacerItem11 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
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
        spacerItem12 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
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
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.txt_ubicacion = QtWidgets.QLineEdit(self.page_delete)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ubicacion.sizePolicy().hasHeightForWidth())
        self.txt_ubicacion.setSizePolicy(sizePolicy)
        self.txt_ubicacion.setMinimumSize(QtCore.QSize(241, 30))
        self.txt_ubicacion.setMaximumSize(QtCore.QSize(241, 30))
        self.txt_ubicacion.setStyleSheet("font-size:18px;\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"border-radius:10px;")
        self.txt_ubicacion.setObjectName("txt_ubicacion")
        self.horizontalLayout_3.addWidget(self.txt_ubicacion)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem17)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
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
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem19)
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
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem20)
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
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem21)
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
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem22)
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
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_add)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
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
        self.verticalLayout_8.addWidget(self.label)
        spacerItem23 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem23)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem24)
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
        self.txt_sedecodigo = QtWidgets.QLineEdit(self.page_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_sedecodigo.sizePolicy().hasHeightForWidth())
        self.txt_sedecodigo.setSizePolicy(sizePolicy)
        self.txt_sedecodigo.setMinimumSize(QtCore.QSize(200, 31))
        self.txt_sedecodigo.setMaximumSize(QtCore.QSize(200, 31))
        self.txt_sedecodigo.setStyleSheet("font-size:18px;\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"border-radius:10px;")
        self.txt_sedecodigo.setReadOnly(True)
        self.txt_sedecodigo.setObjectName("txt_sedecodigo")
        self.horizontalLayout_13.addWidget(self.txt_sedecodigo)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_13)
        self.bt_buscarsede = QtWidgets.QPushButton(self.page_add)
        self.bt_buscarsede.setText("")
        self.bt_buscarsede.setIcon(icon4)
        self.bt_buscarsede.setObjectName("bt_buscarsede")
        self.horizontalLayout_15.addWidget(self.bt_buscarsede)
        spacerItem26 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem26)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        spacerItem27 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem27)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem28 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem28)
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
        self.txt_nombre = QtWidgets.QLineEdit(self.page_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_nombre.sizePolicy().hasHeightForWidth())
        self.txt_nombre.setSizePolicy(sizePolicy)
        self.txt_nombre.setMinimumSize(QtCore.QSize(200, 31))
        self.txt_nombre.setMaximumSize(QtCore.QSize(200, 31))
        self.txt_nombre.setStyleSheet("border:none;\n"
"border-bottom:2px solid white;\n"
"font-size:18px;\n"
"border-radius:10px;")
        self.txt_nombre.setObjectName("txt_nombre")
        self.horizontalLayout_12.addWidget(self.txt_nombre)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_12)
        spacerItem30 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem30)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        spacerItem31 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem31)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem32)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
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
        self.txt_codigoaula = QtWidgets.QLineEdit(self.page_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_codigoaula.sizePolicy().hasHeightForWidth())
        self.txt_codigoaula.setSizePolicy(sizePolicy)
        self.txt_codigoaula.setMinimumSize(QtCore.QSize(200, 31))
        self.txt_codigoaula.setMaximumSize(QtCore.QSize(200, 31))
        self.txt_codigoaula.setStyleSheet("border:none;\n"
"border-bottom:2px solid white;\n"
"font-size:18px;\n"
"border-radius:10px;")
        self.txt_codigoaula.setObjectName("txt_codigoaula")
        self.horizontalLayout_11.addWidget(self.txt_codigoaula)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_11)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem33)
        self.verticalLayout_8.addLayout(self.horizontalLayout_20)
        spacerItem34 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem34)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem35 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem35)
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
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem36)
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
        self.horizontalLayout_17.addLayout(self.horizontalLayout_9)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem37)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.stackedWidget.addWidget(self.page_add)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)
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
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem38)
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
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem39)
        self.bt_salir = QtWidgets.QPushButton(self.centralwidget)
        self.bt_salir.setMinimumSize(QtCore.QSize(75, 31))
        self.bt_salir.setMaximumSize(QtCore.QSize(75, 31))
        self.bt_salir.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_salir.setObjectName("bt_salir")
        self.horizontalLayout.addWidget(self.bt_salir)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_aggView_2.setText(_translate("MainWindow", "Agregar"))
        self.bt_sedes.setText(_translate("MainWindow", "Sedes"))
        self.bt_deleteView.setText(_translate("MainWindow", "Eliminar"))
        self.bt_database.setText(_translate("MainWindow", "Registrados"))
        self.label_12.setText(_translate("MainWindow", "Eliminar Aula"))
        self.label_10.setText(_translate("MainWindow", "Nombre"))
        self.label_11.setText(_translate("MainWindow", "Codigo Sede"))
        self.bt_delete.setText(_translate("MainWindow", "Eliminar"))
        self.label_13.setText(_translate("MainWindow", "Aulas"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ubicacion"))
        self.bt_act.setText(_translate("MainWindow", "Actualizar"))
        self.label.setText(_translate("MainWindow", "Registro de Aulas"))
        self.label_2.setText(_translate("MainWindow", "Sede"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.label_5.setText(_translate("MainWindow", "Codigo"))
        self.bt_clear.setText(_translate("MainWindow", "Limpiar"))
        self.bt_register.setText(_translate("MainWindow", "Registrar"))
        self.bt_salir_2.setText(_translate("MainWindow", "VOLVER"))
        self.label_4.setText(_translate("MainWindow", "Aulas"))
        self.bt_salir.setText(_translate("MainWindow", "SALIR"))
