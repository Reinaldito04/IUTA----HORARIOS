# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/carreras.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:rgb(152, 228, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.bt_back = QtWidgets.QPushButton(self.frame)
        self.bt_back.setMinimumSize(QtCore.QSize(75, 31))
        self.bt_back.setMaximumSize(QtCore.QSize(75, 31))
        self.bt_back.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_back.setObjectName("bt_back")
        self.horizontalLayout_8.addWidget(self.bt_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.bt_salir = QtWidgets.QPushButton(self.frame)
        self.bt_salir.setMinimumSize(QtCore.QSize(75, 31))
        self.bt_salir.setMaximumSize(QtCore.QSize(75, 31))
        self.bt_salir.setStyleSheet("background-color:red;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius:15px;")
        self.bt_salir.setObjectName("bt_salir")
        self.horizontalLayout_8.addWidget(self.bt_salir)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.bt_agg = QtWidgets.QPushButton(self.frame_2)
        self.bt_agg.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_agg.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_agg.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_agg.setIconSize(QtCore.QSize(20, 20))
        self.bt_agg.setObjectName("bt_agg")
        self.verticalLayout_4.addWidget(self.bt_agg)
        self.bt_level = QtWidgets.QPushButton(self.frame_2)
        self.bt_level.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_level.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_level.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_level.setIconSize(QtCore.QSize(20, 20))
        self.bt_level.setObjectName("bt_level")
        self.verticalLayout_4.addWidget(self.bt_level)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.bt_view = QtWidgets.QPushButton(self.frame_2)
        self.bt_view.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_view.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_view.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_view.setIconSize(QtCore.QSize(20, 20))
        self.bt_view.setObjectName("bt_view")
        self.verticalLayout_4.addWidget(self.bt_view)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.bt_edit = QtWidgets.QPushButton(self.frame_2)
        self.bt_edit.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_edit.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_edit.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_edit.setIconSize(QtCore.QSize(20, 20))
        self.bt_edit.setObjectName("bt_edit")
        self.verticalLayout_4.addWidget(self.bt_edit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_14.addWidget(self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_agg = QtWidgets.QWidget()
        self.page_agg.setObjectName("page_agg")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_agg)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.label_2 = QtWidgets.QLabel(self.page_agg)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        spacerItem8 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.label_5 = QtWidgets.QLabel(self.page_agg)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size:15px;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.txt_code = QtWidgets.QLineEdit(self.page_agg)
        self.txt_code.setMinimumSize(QtCore.QSize(191, 21))
        self.txt_code.setMaximumSize(QtCore.QSize(191, 21))
        self.txt_code.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_code.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_code.setObjectName("txt_code")
        self.horizontalLayout_4.addWidget(self.txt_code)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(28, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.label_6 = QtWidgets.QLabel(self.page_agg)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-size:15px;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.txt_name = QtWidgets.QLineEdit(self.page_agg)
        self.txt_name.setMinimumSize(QtCore.QSize(191, 21))
        self.txt_name.setMaximumSize(QtCore.QSize(191, 21))
        self.txt_name.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_name.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_name.setObjectName("txt_name")
        self.horizontalLayout_5.addWidget(self.txt_name)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(28, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.bt_agg_2 = QtWidgets.QPushButton(self.page_agg)
        self.bt_agg_2.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_agg_2.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_agg_2.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_agg_2.setIconSize(QtCore.QSize(20, 20))
        self.bt_agg_2.setObjectName("bt_agg_2")
        self.horizontalLayout_3.addWidget(self.bt_agg_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.page_agg)
        self.page_level = QtWidgets.QWidget()
        self.page_level.setObjectName("page_level")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_level)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem17)
        self.label_16 = QtWidgets.QLabel(self.page_level)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_23.addWidget(self.label_16)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem18)
        self.verticalLayout_17.addLayout(self.horizontalLayout_23)
        spacerItem19 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem19)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem20)
        self.label_17 = QtWidgets.QLabel(self.page_level)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font-size:15px;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_24.addWidget(self.label_17)
        self.txt_code_3 = QtWidgets.QLineEdit(self.page_level)
        self.txt_code_3.setMinimumSize(QtCore.QSize(191, 21))
        self.txt_code_3.setMaximumSize(QtCore.QSize(191, 21))
        self.txt_code_3.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_code_3.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_code_3.setReadOnly(True)
        self.txt_code_3.setObjectName("txt_code_3")
        self.horizontalLayout_24.addWidget(self.txt_code_3)
        self.bt_searchCarrera = QtWidgets.QPushButton(self.page_level)
        self.bt_searchCarrera.setStyleSheet("border-radius:15px;")
        self.bt_searchCarrera.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/baseline-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_searchCarrera.setIcon(icon)
        self.bt_searchCarrera.setObjectName("bt_searchCarrera")
        self.horizontalLayout_24.addWidget(self.bt_searchCarrera)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem21)
        self.verticalLayout_17.addLayout(self.horizontalLayout_24)
        spacerItem22 = QtWidgets.QSpacerItem(28, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem22)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem23)
        self.label_18 = QtWidgets.QLabel(self.page_level)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font-size:15px;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_25.addWidget(self.label_18)
        self.txt_name_5 = QtWidgets.QLineEdit(self.page_level)
        self.txt_name_5.setMinimumSize(QtCore.QSize(191, 21))
        self.txt_name_5.setMaximumSize(QtCore.QSize(191, 21))
        self.txt_name_5.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_name_5.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_name_5.setObjectName("txt_name_5")
        self.horizontalLayout_25.addWidget(self.txt_name_5)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem24)
        self.verticalLayout_17.addLayout(self.horizontalLayout_25)
        spacerItem25 = QtWidgets.QSpacerItem(28, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem26)
        self.bt_agg_5 = QtWidgets.QPushButton(self.page_level)
        self.bt_agg_5.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_agg_5.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_agg_5.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_agg_5.setIconSize(QtCore.QSize(20, 20))
        self.bt_agg_5.setObjectName("bt_agg_5")
        self.horizontalLayout_26.addWidget(self.bt_agg_5)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem27)
        self.verticalLayout_17.addLayout(self.horizontalLayout_26)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.stackedWidget.addWidget(self.page_level)
        self.page_edit = QtWidgets.QWidget()
        self.page_edit.setObjectName("page_edit")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_edit)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.page_edit)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem28)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem29 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem29)
        self.ln_busqueda = QtWidgets.QLineEdit(self.page_edit)
        self.ln_busqueda.setMinimumSize(QtCore.QSize(311, 21))
        self.ln_busqueda.setMaximumSize(QtCore.QSize(311, 21))
        self.ln_busqueda.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(128, 179, 255);")
        self.ln_busqueda.setObjectName("ln_busqueda")
        self.horizontalLayout_9.addWidget(self.ln_busqueda)
        self.bt_search = QtWidgets.QPushButton(self.page_edit)
        self.bt_search.setStyleSheet("border:none;")
        self.bt_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/imagenes/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_search.setIcon(icon1)
        self.bt_search.setIconSize(QtCore.QSize(20, 20))
        self.bt_search.setObjectName("bt_search")
        self.horizontalLayout_9.addWidget(self.bt_search)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem30)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem31)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem32)
        self.label_9 = QtWidgets.QLabel(self.page_edit)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-size:15px;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.txt_name_2 = QtWidgets.QLineEdit(self.page_edit)
        self.txt_name_2.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_name_2.setObjectName("txt_name_2")
        self.horizontalLayout_13.addWidget(self.txt_name_2)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem33)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem34)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem35)
        self.label_10 = QtWidgets.QLabel(self.page_edit)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-size:15px;")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.txt_apell_2 = QtWidgets.QLineEdit(self.page_edit)
        self.txt_apell_2.setStyleSheet("border:none;\n"
"border-bottom: 2px solid rgb(128, 179, 255);\n"
"border-right:2px solid rgb(128, 179, 255);\n"
"border-radius:10px;\n"
"font-size:14px;")
        self.txt_apell_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_apell_2.setObjectName("txt_apell_2")
        self.horizontalLayout_12.addWidget(self.txt_apell_2)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem36)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem37)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem38 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem38)
        self.bt_edit_2 = QtWidgets.QPushButton(self.page_edit)
        self.bt_edit_2.setMinimumSize(QtCore.QSize(91, 41))
        self.bt_edit_2.setMaximumSize(QtCore.QSize(91, 41))
        self.bt_edit_2.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_edit_2.setIconSize(QtCore.QSize(20, 20))
        self.bt_edit_2.setObjectName("bt_edit_2")
        self.horizontalLayout_10.addWidget(self.bt_edit_2)
        spacerItem39 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem39)
        self.bt_delete = QtWidgets.QPushButton(self.page_edit)
        self.bt_delete.setMinimumSize(QtCore.QSize(91, 41))
        self.bt_delete.setMaximumSize(QtCore.QSize(91, 41))
        self.bt_delete.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_delete.setIconSize(QtCore.QSize(20, 20))
        self.bt_delete.setObjectName("bt_delete")
        self.horizontalLayout_10.addWidget(self.bt_delete)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem40)
        self.bt_clear = QtWidgets.QPushButton(self.page_edit)
        self.bt_clear.setMinimumSize(QtCore.QSize(91, 41))
        self.bt_clear.setMaximumSize(QtCore.QSize(91, 41))
        self.bt_clear.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_clear.setIconSize(QtCore.QSize(20, 20))
        self.bt_clear.setObjectName("bt_clear")
        self.horizontalLayout_10.addWidget(self.bt_clear)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem41)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.stackedWidget.addWidget(self.page_edit)
        self.page_view = QtWidgets.QWidget()
        self.page_view.setObjectName("page_view")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_view)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem42)
        self.label_4 = QtWidgets.QLabel(self.page_view)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem43)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.page_view)
        self.tableWidget.setStyleSheet("background-color:rgb(152, 228, 255);\n"
"font-size:14px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem44 = QtWidgets.QSpacerItem(141, 51, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem44)
        self.bt_act = QtWidgets.QPushButton(self.page_view)
        self.bt_act.setMinimumSize(QtCore.QSize(141, 51))
        self.bt_act.setMaximumSize(QtCore.QSize(141, 51))
        self.bt_act.setStyleSheet("border-radius:15px;\n"
"color:white;\n"
"font-size:15px;\n"
"background-color: rgb(104, 126, 255);")
        self.bt_act.setIconSize(QtCore.QSize(20, 20))
        self.bt_act.setObjectName("bt_act")
        self.horizontalLayout.addWidget(self.bt_act)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.stackedWidget.addWidget(self.page_view)
        self.horizontalLayout_14.addWidget(self.stackedWidget)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_back.setText(_translate("MainWindow", "Volver"))
        self.label.setText(_translate("MainWindow", "CARRERAS"))
        self.bt_salir.setText(_translate("MainWindow", "SALIR"))
        self.bt_agg.setText(_translate("MainWindow", "Agregar "))
        self.bt_level.setText(_translate("MainWindow", "Agregar Nivel"))
        self.bt_view.setText(_translate("MainWindow", "Visualizar"))
        self.bt_edit.setText(_translate("MainWindow", "Editar"))
        self.label_2.setText(_translate("MainWindow", "AGREGAR   "))
        self.label_5.setText(_translate("MainWindow", "Codigo"))
        self.label_6.setText(_translate("MainWindow", "Nombre"))
        self.bt_agg_2.setText(_translate("MainWindow", "Agregar "))
        self.label_16.setText(_translate("MainWindow", "Agregar Nivel"))
        self.label_17.setText(_translate("MainWindow", "Carrera"))
        self.label_18.setText(_translate("MainWindow", "Nivel"))
        self.bt_agg_5.setText(_translate("MainWindow", "Agregar Nivel"))
        self.label_3.setText(_translate("MainWindow", "EDITAR"))
        self.label_9.setText(_translate("MainWindow", "Codigo"))
        self.label_10.setText(_translate("MainWindow", "Nombre"))
        self.bt_edit_2.setText(_translate("MainWindow", "Modificar"))
        self.bt_delete.setText(_translate("MainWindow", "Eliminar"))
        self.bt_clear.setText(_translate("MainWindow", "Limpiar"))
        self.label_4.setText(_translate("MainWindow", "VISUALIZAR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        self.bt_act.setText(_translate("MainWindow", "Actualizar"))
