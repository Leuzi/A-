import sys
from clases import Nodo,Parada 
sys.path.append('/')
import math
from time import sleep
#Funcion que carga las matrices
def cargaDatos(nombre):
   
   #Abrimos el archivo que contiene los datos
   archivo = open(nombre,"r")
   global paradas,distancias,estimaciones,conexiones #Datos globalses
   global inicio,meta
   paradas = []
   distancias = []
   estimaciones = []
   conexiones = []
   
   line = '0'
   lineas = 0
   numero =0
   #Obtenemos el numero de paradas del archivo
   while numero == 0:
      line = archivo.readline()
      if len(line) > 0:
         if line[0] is not '#': #Saltamos las que empiecen por #
            numero = line
            numero = int(numero)
   #Datos de las paradas 
   while lineas < numero :
      line = archivo.readline()
      if len(line) > 0:
         if line[0] is not '#':
            line = line.split()
            #Creamos la parada                       
            paradas.append(Parada(lineas,line[0],[line[1],line[2]],[line[3],line[4]]))
            lineas+=1
   
   #Inicializamos las variables globales inicio y parada
   inicio=paradas[0]     
   meta = paradas[0]   
   line = '0'
   lineas = 0
   
   #Creamos las martices de estimaciones
   estimaciones = crearEstimacionesCoordenadas(paradas)
   
   print estimaciones
   
   #Obtenemos la matriz de coste(conexiones)
   while lineas < numero:
      line = archivo.readline()
      if line[0] is not '#':
         line = line.split()
         line2 = line[:]
         for i in range(len(line2)):
            line2[i] = int(line2[i])
            if line2[i] > 0:
               line2[i] -= 1
         print line2
         conexiones.append(line2)
         for i in range(len(line)):
            line[i] = int(line[i])
            if line[i] is not -1:
               #print "cambiar"
               #Creamos los costes
               line[i] = (estimaciones[lineas][i])
            else:
               #print "no cambiar"
               pass
         distancias.append(line)
         lineas+=1
      line = '0'
   print distancias
   print "Conexiones"
   print conexiones
   
   lineas = 0
   #Cerramos el archibo
   archivo.close()
   
   return paradas,distancias,estimaciones,conexiones

def algoritmoA(paradas,matrizCostes,matrizEstimaciones,matrizConexiones,inicio,meta,opcion):
   
   #Creamos el nodo inicial, y las dos listas
   if opcion is 0:
      inicio = Nodo(None,inicio,0,matrizEstimaciones[meta.posicion][inicio.posicion])
   else:
      inicio = Nodo(None,inicio,0,0)
   listaAbierta = set()
   listaCerrada = set()
   listaAbierta.add(inicio)
   
   paso = 0
   #Mientras que haya elementos en las lista abierta
   while len(listaAbierta) >0:
      print "PASO ", paso
      paso = paso +1
      
      print "Lista Abierta"
      for nodo in listaAbierta:
         print nodo
      #Obtenemos el mejor nodo de los posibles en la lista abierta basandonos en su h y g
      actual = min(listaAbierta, key=lambda nodo:int(nodo.g) + int(nodo.h))
     
      print "Seleccionamos " +  actual.parada.nombre
      #Si hemos seleccionado la meta, hemos terminado
      if actual.parada.nombre == meta.nombre:
         ruta = []
         #Obtenemos la ruta al padre 
         while actual.padre is not None:
            ruta.append(actual)
            actual = actual.padre
         ruta.append(actual)
         #Devolvemos la ruta
         return ruta
         break
      #Si no, quitamos el elemento seleccionado de la lista abierta y la ponemos en la lista cerrada
      listaAbierta.remove(actual)
      listaCerrada.add(actual)
      
      #Obtenemos sus descendientes
      posibles = set()
      #sleep(5)
      for i in range(len(matrizCostes[0])):
         if int(matrizCostes[actual.parada.posicion][i]) is not -1:
             if opcion is 0:
               posibles.add(Nodo(actual,paradas[i],actual.g,matrizEstimaciones[meta.posicion][i]))
             else:
               posibles.add(Nodo(actual,paradas[i],actual.g,0))
      
      #Nodos a eliminar(padres y abuelos)
      eliminar = set()
      
      for nodo in posibles:
         if nodo.padre is not None:
            if nodo.padre.parada.nombre == nodo.parada.nombre:
               eliminar.add(nodo)
            else:
               if nodo.padre.padre is not None:
                  if nodo.padre.padre.parada.nombre == nodo.parada.nombre:
                     print "Nodo " +nodo.parada.nombre +" no deberia estar"
                     eliminar.add(nodo)
      
      #Lista final de posibles          
      posibles = posibles.difference(eliminar)
       
      print "Posibles "
      for nodo in posibles :
         #Obtenemos el coste de g
         if opcion is 0:
            tentative_g_score = int(actual.g) + int(matrizCostes[actual.parada.posicion][nodo.parada.posicion])
         else:
            tentative_g_score = int(actual.g) + int(matrizConexiones[actual.parada.posicion][nodo.parada.posicion])
         if nodo in listaCerrada and tentative_g_score >= nodo.g :
               continue
         if nodo not in listaAbierta or tentative_g_score < nodo.g :
            #Si no lo hemos explorado
            nodo.g = tentative_g_score
            if opcion is 0:
               nodo.h = matrizEstimaciones[meta.posicion][nodo.parada.posicion]
            else:
               nodo.h = 0
            if nodo not in listaAbierta :
               listaAbierta.add(nodo)
         print nodo

#Algoritmo greedy
def greedy(paradas,matrizCostes,matrizEstimaciones,inicio,meta):
   
   #Solo cambiamos el proceso de seleccion del nodo mas prometedor
   inicio = Nodo(None,inicio,0,matrizEstimaciones[meta.posicion][inicio.posicion])
   listaAbierta = set()
   listaAbierta.add(inicio)
      
   encontrado = False
   paso = 0
   while not encontrado:
      print "PASO ", paso
      paso = paso +1
      print "Lista Abierta"
      for nodo in listaAbierta:
         print nodo      
      
      #Cogemos el nodo que este mas cerca de la meta
      actual = None
      for nodo in listaAbierta:
         if actual is not None:
            if actual.h > nodo.h:
               actual = nodo
         else:
            actual = nodo
      
      listaAbierta = set()
      listaAbierta.add(actual)
      print "Seleccionamos ," + actual.parada.nombre
      #Nodo es meta
      if actual.parada.nombre is meta.nombre:
         if actual.parada.nombre is meta.nombre:
            encontrado = True
      #Nodos descendientes del actual
      else:
         posibles = set()
         #sleep(5)
         for i in range(len(matrizCostes[0])):
            if int(matrizCostes[actual.parada.posicion][i]) is not -1:
                posibles.add(Nodo(actual,paradas[i],actual.g,matrizEstimaciones[meta.posicion][i]))
         
         eliminar = set()
         print "Nodos posibles"
         for nodo in posibles:
             if nodo.padre is not None:
               if nodo.padre.parada.nombre == nodo.parada.nombre:
                  eliminar.add(nodo)
               else:
                  if nodo.padre.padre is not None:
                     if nodo.padre.padre.parada.nombre == nodo.parada.nombre:
                        print "Nodo " +nodo.parada.nombre +" no deberia estar"
                        eliminar.add(nodo)
                     
         listaAbierta = posibles.difference(eliminar)
         
         for nodo in listaAbierta:
            print nodo.parada.nombre            
 
         if not listaAbierta:
            encontrado = True
   ruta = []
   #Obtenemos ruta
   while actual.padre is not None:
      ruta.append(actual)
      actual = actual.padre
   ruta.append(actual)
   return ruta
         
   

infinito = float("inf")
def IDA(paradas,distancias,matrizEstimaciones,inicio,meta):
   
   while True:
      solucion, limite = DLS(inicio,paradas,distancias,matrizEstimaciones,inicio,meta)
      if solucion != None:
         return solucion
      if limite == infinitio:
         return None
 
# returns (solution-sequence or None, new cost limit)
def DLS(actual, paradas,distancias,matrizEstimaciones,inicio,meta):
    #actual = last_element(path_so_far)
    minimo = actual.g + actual.h
    if minimo > limite:
        return None, minimo
    if actual.parada.nombre == meta.nombre:
        return actual, limite
 
    siguiente = infinito
    soluciones = []

    posibles = set()
    #sleep(5)
    for i in range(len(matrizCostes[0])):
       if int(matrizCostes[actual.parada.posicion][i]) is not -1:
           posibles.add(Nodo(actual,paradas[i],actual.g,matrizEstimaciones[meta.posicion][i]))
   
    eliminar = set()
    print "Nodos posibles"
    for nodo in posibles:
        if nodo.padre is not None:
          if nodo.padre.parada.nombre == nodo.parada.nombre:
             eliminar.add(nodo)
          else:
             if nodo.padre.padre is not None:
                if nodo.padre.padre.parada.nombre == nodo.parada.nombre:
                   print "Nodo " +nodo.parada.nombre +" no deberia estar"
                   eliminar.add(nodo)
                        
    posibles = posibles.difference(eliminar)

   
    for nodo in posibles:
        nuevo = nodo.g+nodo.h
        solucion, nuevo_coste = DLS(nodo, paradas,distancias,matrizEstimaciones,inicio,meta)
        if solucion != None:
            solutiones.append([solucion, nuevo_coste])
        siguiente = min(siguiente, nuevo_coste)
 
    if len(soluciones) > 0:
      return min(solutiones, key=lambda o:o[1])
    return None, siguiente

#Crea una matriz de distancias entre dos paradas
def crearEstimacionesCoordenadas(paradas):
   
   #Matriz de estimaciones
   estimaciones = []
   
   for i in range(len(paradas)):
      #Vector de distancias
      distancias= []
      for j in range(len(paradas)):
         dx = paradas[i].coordenadas[0]-paradas[j].coordenadas[0] #Diferencia de x
         dy = paradas[i].coordenadas[1]-paradas[j].coordenadas[1] #Diferencia de y
         distancia = int(math.sqrt(dx*dx+dy*dy))   #distancia al cuadrado 
         distancias.append(distancia)
      estimaciones.append(distancias)   
   return estimaciones   
   
