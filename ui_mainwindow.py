# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(651, 503)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_agregar_inicio = QPushButton(self.frame)
        self.pushButton_agregar_inicio.setObjectName(u"pushButton_agregar_inicio")

        self.gridLayout_2.addWidget(self.pushButton_agregar_inicio, 8, 0, 1, 2)

        self.spinBox_destino_y = QSpinBox(self.frame)
        self.spinBox_destino_y.setObjectName(u"spinBox_destino_y")
        self.spinBox_destino_y.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_destino_y, 3, 1, 1, 1)

        self.spinBox_green = QSpinBox(self.frame)
        self.spinBox_green.setObjectName(u"spinBox_green")
        self.spinBox_green.setMaximum(255)

        self.gridLayout_2.addWidget(self.spinBox_green, 6, 1, 1, 1)

        self.pushButton_ID = QPushButton(self.frame)
        self.pushButton_ID.setObjectName(u"pushButton_ID")

        self.gridLayout_2.addWidget(self.pushButton_ID, 12, 0, 1, 2)

        self.spinBox_red = QSpinBox(self.frame)
        self.spinBox_red.setObjectName(u"spinBox_red")
        self.spinBox_red.setMaximum(255)

        self.gridLayout_2.addWidget(self.spinBox_red, 5, 1, 1, 1)

        self.pushButton_DISTANCIA = QPushButton(self.frame)
        self.pushButton_DISTANCIA.setObjectName(u"pushButton_DISTANCIA")

        self.gridLayout_2.addWidget(self.pushButton_DISTANCIA, 13, 0, 1, 2)

        self.pushButton_mostrar = QPushButton(self.frame)
        self.pushButton_mostrar.setObjectName(u"pushButton_mostrar")

        self.gridLayout_2.addWidget(self.pushButton_mostrar, 11, 0, 1, 2)

        self.label_velocidad = QLabel(self.frame)
        self.label_velocidad.setObjectName(u"label_velocidad")

        self.gridLayout_2.addWidget(self.label_velocidad, 4, 0, 1, 1)

        self.spinBox_origen_x = QSpinBox(self.frame)
        self.spinBox_origen_x.setObjectName(u"spinBox_origen_x")
        self.spinBox_origen_x.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_origen_x, 0, 1, 1, 1)

        self.spinBox_velocidad = QSpinBox(self.frame)
        self.spinBox_velocidad.setObjectName(u"spinBox_velocidad")
        self.spinBox_velocidad.setMinimum(-214748364)
        self.spinBox_velocidad.setMaximum(214748364)

        self.gridLayout_2.addWidget(self.spinBox_velocidad, 4, 1, 1, 1)

        self.spinBox_blue = QSpinBox(self.frame)
        self.spinBox_blue.setObjectName(u"spinBox_blue")
        self.spinBox_blue.setMaximum(255)

        self.gridLayout_2.addWidget(self.spinBox_blue, 7, 1, 1, 1)

        self.label_blue = QLabel(self.frame)
        self.label_blue.setObjectName(u"label_blue")

        self.gridLayout_2.addWidget(self.label_blue, 7, 0, 1, 1)

        self.label_origen_x = QLabel(self.frame)
        self.label_origen_x.setObjectName(u"label_origen_x")

        self.gridLayout_2.addWidget(self.label_origen_x, 0, 0, 1, 1)

        self.pushButton_VELOCIDAD = QPushButton(self.frame)
        self.pushButton_VELOCIDAD.setObjectName(u"pushButton_VELOCIDAD")

        self.gridLayout_2.addWidget(self.pushButton_VELOCIDAD, 14, 0, 1, 2)

        self.pushButton_agregar_final = QPushButton(self.frame)
        self.pushButton_agregar_final.setObjectName(u"pushButton_agregar_final")

        self.gridLayout_2.addWidget(self.pushButton_agregar_final, 9, 0, 1, 2)

        self.spinBox_destino_x = QSpinBox(self.frame)
        self.spinBox_destino_x.setObjectName(u"spinBox_destino_x")
        self.spinBox_destino_x.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_destino_x, 2, 1, 1, 1)

        self.label_destino_x = QLabel(self.frame)
        self.label_destino_x.setObjectName(u"label_destino_x")

        self.gridLayout_2.addWidget(self.label_destino_x, 2, 0, 1, 1)

        self.label_red = QLabel(self.frame)
        self.label_red.setObjectName(u"label_red")

        self.gridLayout_2.addWidget(self.label_red, 5, 0, 1, 1)

        self.label_green = QLabel(self.frame)
        self.label_green.setObjectName(u"label_green")

        self.gridLayout_2.addWidget(self.label_green, 6, 0, 1, 1)

        self.label_origen_y = QLabel(self.frame)
        self.label_origen_y.setObjectName(u"label_origen_y")

        self.gridLayout_2.addWidget(self.label_origen_y, 1, 0, 1, 1)

        self.spinBox_origen_y = QSpinBox(self.frame)
        self.spinBox_origen_y.setObjectName(u"spinBox_origen_y")
        self.spinBox_origen_y.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_origen_y, 1, 1, 1, 1)

        self.label_destino_y = QLabel(self.frame)
        self.label_destino_y.setObjectName(u"label_destino_y")

        self.gridLayout_2.addWidget(self.label_destino_y, 3, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 10, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab_3)
        self.salida.setObjectName(u"salida")

        self.gridLayout_5.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Buscar_lineEdit = QLineEdit(self.tab_4)
        self.Buscar_lineEdit.setObjectName(u"Buscar_lineEdit")
        self.Buscar_lineEdit.setDragEnabled(False)

        self.gridLayout_3.addWidget(self.Buscar_lineEdit, 11, 0, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_4)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton, 11, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_4)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 10, 2)

        self.pushButton_DISTANCIA_2 = QPushButton(self.tab_4)
        self.pushButton_DISTANCIA_2.setObjectName(u"pushButton_DISTANCIA_2")

        self.gridLayout_3.addWidget(self.pushButton_DISTANCIA_2, 8, 2, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_4)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 11, 1, 1, 1)

        self.pushButton_VELOCIDAD_2 = QPushButton(self.tab_4)
        self.pushButton_VELOCIDAD_2.setObjectName(u"pushButton_VELOCIDAD_2")

        self.gridLayout_3.addWidget(self.pushButton_VELOCIDAD_2, 9, 2, 1, 1)

        self.pushButton_ID_2 = QPushButton(self.tab_4)
        self.pushButton_ID_2.setObjectName(u"pushButton_ID_2")

        self.gridLayout_3.addWidget(self.pushButton_ID_2, 7, 2, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 8)

        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(1000)

        self.gridLayout_4.addWidget(self.spinBox, 1, 1, 1, 1)

        self.dibujar = QPushButton(self.tab)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_4.addWidget(self.dibujar, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.tab)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider, 1, 2, 1, 1)

        self.limpiar = QPushButton(self.tab)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_4.addWidget(self.limpiar, 1, 7, 1, 1)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 1, 5, 1, 1)

        self.pushButton_agregar = QPushButton(self.tab)
        self.pushButton_agregar.setObjectName(u"pushButton_agregar")

        self.gridLayout_4.addWidget(self.pushButton_agregar, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 651, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_agregar_inicio.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.pushButton_ID.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.pushButton_DISTANCIA.setText(QCoreApplication.translate("MainWindow", u"DISTANCIA", None))
        self.pushButton_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"BLUE", None))
        self.label_origen_x.setText(QCoreApplication.translate("MainWindow", u"Origen_x", None))
        self.pushButton_VELOCIDAD.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD", None))
        self.pushButton_agregar_final.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.label_destino_x.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"RED:", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"GREEN:", None))
        self.label_origen_y.setText(QCoreApplication.translate("MainWindow", u"Origen_y", None))
        self.label_destino_y.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_DISTANCIA_2.setText(QCoreApplication.translate("MainWindow", u"DISTANCIA", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_VELOCIDAD_2.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD", None))
        self.pushButton_ID_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Graficar", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"GRAFO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Fuerza Bruta", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Dijkstra", None))

        self.pushButton_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar PARTICULAS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Grafica", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

