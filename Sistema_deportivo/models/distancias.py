

class Distancias:
    def __init__(self, distancia=None, origen=None, destino=None):
        self.__distancia = distancia
        self.__origen = origen

    @property
    def distancia(self):
        return self.__distancia
    
    @distancia.setter
    def distancia(self, distancia):
        self.__distancia = distancia
    
    @property
    def origen(self):
        return self.__origen
    
    @origen.setter
    def origen(self, origen):
        self.__origen = origen