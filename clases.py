class Parada:
   
   def __init__(self,posicion,nombre,coordenadas,pixeles):
      self.posicion=posicion
      self.nombre=nombre
      self.coordenadas=coordenadas
      self.coordenadas[0]=int(self.coordenadas[0])
      self.coordenadas[1]=int(self.coordenadas[1])
      self.pixeles=pixeles
      self.pixeles[0]=int(self.pixeles[0])
      self.pixeles[1]=int(self.pixeles[1])  
   def __str__(self):
      return self.nombre
      
class Nodo:
   
   def __init__(self,padre,parada,g,h):
      self.padre=padre
      self.parada=parada
      self.g=int(g)
      self.h=int(h)
   def __str__(self):
      return self.parada.nombre + " g:" + str(self.g) + " h:" + str(self.h) + " f:" + str(int(self.g)+int(self.h))
      

