# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created: Thu May 30 19:13:11 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import algoritmos

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Interfaz(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(973, 500)
        self.botonEmpezar = QtGui.QPushButton(Dialog)
        self.botonEmpezar.setGeometry(QtCore.QRect(40, 410, 81, 51))
        self.botonEmpezar.setObjectName(_fromUtf8("botonEmpezar"))
        self.botonReset = QtGui.QPushButton(Dialog)
        self.botonReset.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.botonReset.setObjectName(_fromUtf8("botonReset"))
        self.listaRuta = QtGui.QListWidget(Dialog)
        self.listaRuta.setGeometry(QtCore.QRect(820, 40, 141, 391))
        self.listaRuta.setObjectName(_fromUtf8("listaRuta"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(820, 20, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Mapa = QtGui.QGraphicsView(Dialog)
        self.Mapa.setGeometry(QtCore.QRect(170, 40, 641, 451))
        self.Mapa.setObjectName(_fromUtf8("Mapa"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(180, 20, 121, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 151, 241))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listaInicio = QtGui.QComboBox(self.layoutWidget)
        self.listaInicio.setObjectName(_fromUtf8("listaInicio"))
        self.verticalLayout.addWidget(self.listaInicio)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.listaFin = QtGui.QComboBox(self.layoutWidget)
        self.listaFin.setObjectName(_fromUtf8("listaFin"))
        self.verticalLayout.addWidget(self.listaFin)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.listaAlgoritmo = QtGui.QComboBox(self.layoutWidget)
        self.listaAlgoritmo.setObjectName(_fromUtf8("listaAlgoritmo"))
        self.verticalLayout.addWidget(self.listaAlgoritmo)
        self.botonCancelar = QtGui.QPushButton(Dialog)
        self.botonCancelar.setGeometry(QtCore.QRect(820, 440, 121, 41))
        self.botonCancelar.setObjectName(_fromUtf8("botonCancelar"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.listaSeleccion = QtGui.QComboBox(self.layoutWidget)
        self.listaSeleccion.setObjectName(_fromUtf8("listaSeleccion"))
        self.verticalLayout.addWidget(self.listaSeleccion)




        self.imagen = QtGui.QGraphicsPixmapItem(QtGui.QPixmap("mapa.jpg"));
        self.scene= QtGui.QGraphicsScene()
        self.Mapa.setScene(self.scene)
        self.scene.addItem(self.imagen)
        self.retranslateUi(Dialog)
        
        #Slots de QT (funciones que hay conectar con los elementos de la interfaz)
        QtCore.QObject.connect(self.botonReset, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reiniciar)
        QtCore.QObject.connect(self.botonEmpezar, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.empezar)
        QtCore.QObject.connect(self.listaInicio, QtCore.SIGNAL(_fromUtf8("currentIndexChanged (int)")),Dialog.cambiarInicio)
        QtCore.QObject.connect(self.listaFin, QtCore.SIGNAL(_fromUtf8("currentIndexChanged (int)")),Dialog.cambiarFin)
        QtCore.QObject.connect(self.botonCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")),Dialog.cerrar)
        QtCore.QObject.connect(self.listaAlgoritmo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged (int)")),Dialog.cambiarAlgoritmo)
        QtCore.QObject.connect(self.listaSeleccion, QtCore.SIGNAL(_fromUtf8("currentIndexChanged (int)")),Dialog.cambiarOpcion)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Practica Final IA 2013", None))
        self.botonEmpezar.setText(_translate("Dialog", "Empezar", None))
        self.botonReset.setText(_translate("Dialog", "Reset", None))
        self.label_5.setText(_translate("Dialog", "Solución", None))
        self.label_6.setText(_translate("Dialog", "Mapa", None))
        self.label.setText(_translate("Dialog", "Inicio", None))
        self.label_2.setText(_translate("Dialog", "Meta", None))
        self.label_4.setText(_translate("Dialog", "Algoritmo", None))
        self.label_3.setText(_translate("Dialog", "Seleccion",None))
        self.botonCancelar.setText(_translate("Dialog","Salir",None))
        
        #Rellenamos los elementos de las listas
        for parada in algoritmos.paradas:
            self.listaInicio.addItem(_fromUtf8(str(parada.nombre)))
            self.listaFin.addItem(_fromUtf8(str(parada.nombre)))
        
        
        self.listaAlgoritmo.addItem(_fromUtf8(str("A*")))
        self.listaAlgoritmo.addItem(_fromUtf8(str("Greedy")))
        self.listaSeleccion.addItem(_fromUtf8(str("Distancia")))
        self.listaSeleccion.addItem(_fromUtf8(str("Transbordos")))   

   #Acutalizamos la interfaz con la ruta dada    
    def actualizarLista(self,ruta):
      ruta=ruta[::-1]
            
      color = QtGui.QColor(0,0,0)
      #Brochas y pinceles(cosas de Qt)
      brocha = QtGui.QBrush(QtCore.Qt.black)
      pincel = QtGui.QPen(color,8)
      anterior = None
      #Para cada nodo en la ruta
      for nodo in ruta:
         #Añadimos su nombre a la lista
         self.listaRuta.addItem(_fromUtf8(str(nodo.parada.nombre)+"  "+ str(nodo.g+nodo.h)))
         #Pintamos una elipse y una linea entre ellas
         self.scene.addEllipse(QtCore.QRectF(QtCore.QPointF(nodo.parada.pixeles[0],nodo.parada.pixeles[1]),QtCore.QSizeF(QtCore.QSize(12,12))),pincel,brocha)
         if anterior is not None:
            self.scene.addLine(anterior.parada.pixeles[0]+6,anterior.parada.pixeles[1]+6,nodo.parada.pixeles[0]+6,nodo.parada.pixeles[1]+6,pincel)
         anterior = nodo   
    
    #Borramos lo que habia en la escena y cargamos el mapa otra vez     
    def reiniciarMapa(self):
      self.imagen = QtGui.QGraphicsPixmapItem(QtGui.QPixmap("mapa.jpg"));
      self.scene= QtGui.QGraphicsScene()
      self.Mapa.setScene(self.scene)
      self.scene.addItem(self.imagen)   

