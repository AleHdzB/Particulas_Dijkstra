from PySide2.QtWidgets import QMainWindow,QFileDialog, QMessageBox,QTableWidgetItem, QMessageBox, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow 
from PySide2.QtGui import QPen, QColor, QTransform
from particula import Particula
from admin_particulas import Admin
from random import randint
from pprint import pprint
from algoritmos import *
from grafo import Grafo

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.puntos = []
        self.grafo = Grafo()
        self.admin = Admin()
        #Declaracion de objeto escena
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        #Botones
        self.ui.pushButton_agregar_inicio.clicked.connect(self.click_agregar_inicio)
        self.ui.pushButton_agregar_final.clicked.connect(self.click_agregar_final)
        self.ui.pushButton_mostrar.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)


        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)
        #Mostrar ordenadas (Sort)
        self.ui.pushButton_ID.clicked.connect(self.ordenar_id_ascendente_qplantextedit)
        self.ui.pushButton_ID_2.clicked.connect(self.ordenar_id_ascendente_qtablewidget)

        self.ui.pushButton_DISTANCIA.clicked.connect(self.ordenar_distancia_qplanedit)
        self.ui.pushButton_DISTANCIA_2.clicked.connect(self.ordenar_distancia_qtablewidget)

        self.ui.pushButton_VELOCIDAD.clicked.connect(self.ordenar_velocidad_qplanedit)
        self.ui.pushButton_VELOCIDAD_2.clicked.connect(self.ordenar_velocidad_qtablewidget)


#--------------------------------ALGORITMOS--------------------------------------------
#------------------------------Agregar puntos------------------------------------------   
        self.ui.spinBox.valueChanged[int].connect(self.spinBox_puntos)
        self.ui.horizontalSlider.valueChanged[int].connect(self.slider_puntos)     
        self.ui.pushButton_agregar.clicked.connect(self.agregar_puntos)

    @Slot(int)
    def agregar_puntos(self,n):
        n = self.ui.spinBox.value()  # Obtener el valor del spinBox
        for _ in range(n):
                origen_x = randint(0, 500)
                origen_y = randint(0, 500)
                destino_x = randint(0, 500)
                destino_y = randint(0, 500)
                velocidad = randint(1, 10)
                red = randint(0, 255)
                green = randint(0, 255)
                blue = randint(0, 255)
                particula = Particula(origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
                self.admin.agregar_inicio(particula)  
    @Slot()
    def dibujar(self):
        algoritmo = self.ui.comboBox.currentText()
        self.puntos = get_puntos(self.admin)
        grafo = Grafo()
        pen = QPen()
        pen.setWidth(2)
#------------------------------Mostrar puntos------------------------------------------   
        if (algoritmo == "Puntos"):
                pen = QPen()
                pen.setWidth(2)          
                for punto in self.puntos:
                        x = punto[0]
                        y = punto[1]
                        r = punto[2]
                        g = punto[3]
                        b = punto[4]
                        color = QColor(r,g,b)
                        pen.setColor(color)  
                        self.scene.addEllipse(x,y,6,6,pen)   #(x,y,diametro1,diametro2)
#------------------------------Mostrar GRAFO------------------------------------------                          
        elif(algoritmo == "GRAFO"):
             grafo = Grafo()
             grafo.agregar_vertices_de_particulas(self.admin)
             grafo.agregar_aristas_entre_particulas(self.admin)
             pen = QPen()
             pen.setWidth(1)

            # Dibujar vértices
             for vertice in grafo.obtener_vertices():
                     x = vertice[0]
                     y = vertice[1]
                     self.scene.addEllipse(x, y, 6, 6, pen)

             # Dibujar aristas
             for vertice, aristas in grafo.vertices.items():
                     for arista in aristas:
                        destino = arista[0]
                        x1, y1 = vertice
                        x2, y2 = destino
                        self.scene.addLine(x1+3, y1+3, x2+3, y2+3, pen)

#------------------------------FUERZA BRUTA--------------------------------------------        
        elif(algoritmo == "Fuerza Bruta"):
                resultado = fuerza_bruta(self.puntos)
                pen = QPen()
                pen.setWidth(3)
                for punto1, punto2 in resultado:
                        x1 = punto1[0]
                        y1 = punto1[1]
                        x2 = punto2[0]
                        y2 = punto2[1]
                        r = 255
                        g = 0
                        b = 0
                        color = QColor(r,g,b)
                        pen.setColor(color)
                        self.scene.addLine(x1+3,y1+3,x2+3,y2+3,pen)        
#------------------------------Dijkstra--------------------------------------------                           
        elif(algoritmo == "Dijkstra"):
                print("Dijkstra")
                grafo.agregar_vertices_de_particulas(self.admin)
                grafo.agregar_aristas_entre_particulas(self.admin)
                vertices = grafo.obtener_vertices()
                inicio = vertices[0]
                distancias, predecesores = dijkstra(grafo, inicio)
                # Pintar las líneas de los caminos más cortos en rojo
                pen = QPen(QColor(255, 0, 0))  # Rojo
                pen.setWidth(3)
                for nodo, predecesor in predecesores.items():
                    if predecesor is not None:
                        x1, y1 = nodo
                        x2, y2 = predecesor
                        self.scene.addLine(x1 + 3, y1 + 3, x2 + 3, y2 + 3, pen)
                for nodo, distancia in distancias.items():
                    print(f"Distancia más corta desde {inicio} hasta {nodo}: {distancia}")               
        elif(algoritmo == "Graficar"):
                for particula in self.admin:
                        r = particula.red
                        g = particula.green
                        b = particula.blue
                        color = QColor(r,g,b)
                        pen.setColor(color)

                        x_origen = particula.origen_x
                        y_origen = particula.origen_y 
                        x_destino = particula.destino_x
                        y_destino = particula.destino_y

                        #Origen (0,0)
                        self.scene.addEllipse(x_origen,y_origen,6,6,pen)   #(x,y,diametro1,diametro2)
                        self.scene.addEllipse(x_destino,y_destino,6,6,pen)
                        self.scene.addLine(x_origen+3,y_origen+3,x_destino+3,y_destino+3,pen)
      
    #Mostrar ordenadas en QplanTexEdit(Sort)
    @Slot()
    def ordenar_id_ascendente_qplantextedit(self):
        self.admin.ordenar_particulas_por_id()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.admin))

    @Slot()
    def ordenar_distancia_qplanedit(self):
        self.admin.ordenar_particulas_por_distancia()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.admin))

    @Slot()
    def ordenar_velocidad_qplanedit(self):
        self.admin.ordenar_particulas_por_velocidad()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.admin))

    #Mostrar ordenadas en QTableWidget(Sort)
    @Slot()
    def ordenar_id_ascendente_qtablewidget(self):
        self.admin.ordenar_particulas_por_id()
        self.mostrar_tabla()
    @Slot()
    def ordenar_distancia_qtablewidget(self):
        self.admin.ordenar_particulas_por_distancia()
        self.mostrar_tabla()
        
    @Slot()
    def ordenar_velocidad_qtablewidget(self):
        self.admin.ordenar_particulas_por_velocidad()
        self.mostrar_tabla()



    @Slot(int)
    def spinBox_puntos(self, x):
        #print(x)
        self.ui.horizontalSlider.setValue(x)

    @Slot(int)
    def slider_puntos(self, x):
      #print(x)
      self.ui.spinBox.setValue(x)
    @Slot()
    def limpiar(self):
        self.scene.clear()

    #Zoom
    def wheelEvent(self,event):
        #print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)

    @Slot()
    def buscar_id(self):
       # print("Buscar ID")
        id = self.ui.Buscar_lineEdit.text()

        encontrado = False
        for particula in self.admin:
            if int(id) == particula.id:
                self.ui.tabla.clear() #Limpiar tabla
                self.ui.tabla.setColumnCount(10) #Config. numero de columnas
                headers = ["ID","ORIGEN_X","ORIGEN_Y","DESTINO_X","DESTINO_Y","VELOCIDAD","RED",
                        "BLUE","GREEN","DISTANCIA"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)  #Headers de Columnas
                self.ui.tabla.setRowCount(1)#Config Filas
                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))   
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                blue_widget = QTableWidgetItem(str(particula.blue))
                green_widget = QTableWidgetItem(str(particula.green))
                distancia_widget = QTableWidgetItem(str(particula.distancia))    

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, blue_widget)
                self.ui.tabla.setItem(0, 8, green_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el identificador "(id)" no fue encontrado'
            )


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10) #Config. numero de columnas
        headers = ["ID","ORIGEN_X","ORIGEN_Y","DESTINO_X","DESTINO_Y","VELOCIDAD","RED",
                   "BLUE","GREEN","DISTANCIA"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)  #Headers de Columnas

        self.ui.tabla.setRowCount(len(self.admin)) #Config. numero de Filas

        row = 0
        for particula in self.admin:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))   
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            blue_widget = QTableWidgetItem(str(particula.blue))
            green_widget = QTableWidgetItem(str(particula.green))
            distancia_widget = QTableWidgetItem(str(particula.distancia))    

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, blue_widget)
            self.ui.tabla.setItem(row, 8, green_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1
    @Slot()
    def action_Abrir_Archivo(self):
        #print("Abrir_Archivo")
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'   
        )[0]
        print(ubicacion)
        if self.admin.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo ABRIR el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "NO se pudo ABRIR el archivo " + ubicacion
            )

    @Slot()
    def action_Guardar_Archivo(self):
        print("Guardar_Archivo")
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON(*.json)'
        )[0]
        print(ubicacion)
        if self.admin.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "NO se pudo crear el archivo" + ubicacion
            )
      
    
    @Slot()
    def click_agregar_inicio(self):
        origen_x = self.ui.spinBox_origen_x.value()
        origen_y = self.ui.spinBox_origen_y.value()
        destino_x = self.ui.spinBox_destino_x.value()
        destino_y = self.ui.spinBox_destino_y.value()
        velocidad = self.ui.spinBox_velocidad.value()
        red = self.ui.spinBox_red.value()
        green = self.ui.spinBox_green.value()
        blue = self.ui.spinBox_blue.value()

        particula = Particula(origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.admin.agregar_inicio(particula)        
           
    @Slot()
    def click_agregar_final(self):
        origen_x = self.ui.spinBox_origen_x.value()
        origen_y = self.ui.spinBox_origen_y.value()
        destino_x = self.ui.spinBox_destino_x.value()
        destino_y = self.ui.spinBox_destino_y.value()
        velocidad = self.ui.spinBox_velocidad.value()
        red = self.ui.spinBox_red.value()
        green = self.ui.spinBox_green.value()
        blue = self.ui.spinBox_blue.value()

        particula = Particula(origen_x, origen_y,destino_x, destino_y, velocidad, red, green, blue)
        self.admin.agregar_final(particula)   
        
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.admin))

    
