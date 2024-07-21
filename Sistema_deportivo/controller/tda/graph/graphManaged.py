from controller.tda.graph.graph import Graph
from controller.tda.linked.linkedList import Linked_List
from controller.exception.arrayPositionException import ArrayPositionException
from controller.tda.graph.adjacent import Adjacent
from math import nan

class GraphManaged(Graph):
    def __init__(self, num_vert) -> None:
        super().__init__()
        self.__numVert = num_vert
        self.__numEdg = 0
        self.__listAdjacent = []
        for i in range(0, num_vert):
            self.__listAdjacent.append(Linked_List())

#                                  GETTERS AND SETTERS
#//////////////////////////////////////////////////////////////////////////////////////
    def setNumEdg(self, number):
        self.__numEdg = number

    @property
    def num_vertex(self):
        return self.__numVert
    
    @property
    def num_edges(self):
        return self.__numEdg
    
#//////////////////////////////////////////////////////////////////////////////////////

    def exist_edges(self, v1, v2): 
        band = False
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            listAdj = self.__listAdjacent[v1]
            if not listAdj.isEmpty:
                arraAdj = listAdj.toArray
                for i in range(0, listAdj._length):
                    adj = arraAdj[i]
                    if adj._destination == v2:
                        band = True
                        break         
        else:
            raise ArrayPositionException("Delimite out - 1")
        return band

#//////////////////////////////////////////////////////////////////////////////////////
# EL METODO WEIGHT EDGES DEVUELVE EL PESO DE UNA ARISTA
    def weight_edges(self, v1, v2):
        weight = None
        if self.exist_edges(v1, v2):
            if v1 <= self.num_vertex and v2 <= self.num_vertex:
                listAdj = self.__listAdjacent[v1]
                if not listAdj.isEmpty():
                    arraAdj = listAdj.toArray
                    for i in range(0, listAdj._length):
                        adj = arraAdj[i]
                        if adj._destination == v2:
                            weight = adj._weight
                            break         
            else:
                raise ArrayPositionException("Delimite out - 2")
        return weight

#//////////////////////////////////////////////////////////////////////////////////////           
    def insert_edges_weight(self, v1, v2, weight):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            if not self.exist_edges(v1, v2):
               self.__numEdg += 1
               adj = Adjacent()
               adj._destination = v2
               adj._weight = weight
               print("hasta aquiiiiii")
               self.__listAdjacent[v1].add(adj, self.__listAdjacent[v1]._length)
               self.paint_graph()
        else:
            raise ArrayPositionException("Delimite out")

#//////////////////////////////////////////////////////////////////////////////////////   
# metodos para insertar aristas, adyacencias y vertices       
    def insert_edges(self, v1, v2):
        self.insert_edges_weight(v1, v2, nan)
        
    def adjacent(self, v1):
        return self.__listAdjacent[v1]
    
    def insert_vertex(self):
        self.__numVert += 1
        self.__listAdjacent.append(Linked_List())
        self.paint_graph()

#//////////////////////////////////////////////////////////////////////////////////////