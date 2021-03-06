#!/usr/bin/python
import array
import sys
sys.path.append('/')

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QHBoxLayout, QLabel,
        QPushButton)
from interfaz import Interfaz
from algoritmos import *
class Principal(QtGui.QMainWindow):
    #Creamos un Widget
    #Le asignamos el correspondiente Ui
    #Lo colocamos
    #definimos los slots

    def __init__(self,parent=None):

        global paradas
        global distancias
        global estimaciones
        global inicio
        global meta
        global algoritmo
        global conexiones
        global opciones
        #Cargamos los datos
        paradas, distancias,estimaciones,conexiones =  cargaDatos("datos")

        algoritmo = 0  
        opciones = 0      

        inicio = paradas[0]
        meta = paradas[0]
        #Creamos la interfaz
        QtGui.QWidget.__init__(self,parent)
        self.ui=Interfaz()
        self.ui.setupUi(self)

    #Boton reiniciar 
    def reiniciar(self):
      self.ui.listaRuta.clear()
      self.ui.reiniciarMapa()
    
    #Boton cerrar
    def cerrar(self):
      sys.exit()
    
    #Boton empezar
    def empezar(self):
      
      self.reiniciar()
      global algoritmo
      print algoritmo
      global opciones
      if algoritmo is 1:
         ruta = greedy(paradas,distancias,estimaciones,inicio,meta)
      else:
         ruta = algoritmoA(paradas,distancias,estimaciones,conexiones,inicio,meta,opciones)      
      print "El resultado es"
      for nodo in ruta:
         print nodo
      self.ui.actualizarLista(ruta)
      #Algoritmo para resaltar resultado
    
    #Lista de cambio de estacion de inicio
    def cambiarInicio(self,pos):
      global inicio
      inicio = paradas[pos]
    #Lista de cambio de estacion de meta
    def cambiarFin(self,pos):
      global meta
      meta = paradas[pos]
    #Lista de cambio de algoritmo
    def cambiarAlgoritmo(self,pos):
      global algoritmo
      algoritmo = pos
    
    #Lista de cambio de algoritmo
    def cambiarOpcion(self,pos):
      global opciones
      opciones = pos
      print opciones

def main():
   
      #Se crea la interfaz de usuario
      app = QtGui.QApplication(sys.argv)
      #Creamos el formulario principal
      myapp = Principal()
      #Mostramos el formulario
      myapp.show()
      #Ejecutamos
      sys.exit(app.exec_())
      

      inicio = paradas[0]
      meta = paradas[-1]
      ruta = algoritmoA(paradas,distancias,estimaciones,inicio,meta)
      print ruta
      for nodo in ruta:
         print nodo  

if __name__ == "__main__":
    main()
