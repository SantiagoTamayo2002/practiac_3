
import numpy as np
import json

#------------------------------------------------------------------------------
#------------------------------Algoritmo de Floyd------------------------------
class Floyd:
    def __init__(self, graph:object=None, start:int=0, end:int=0):
        self.__graph = graph
        self.__matrix = np.zeros((self.__graph.num_vertex, self.__graph.num_vertex))
        self.__matrixParent = np.zeros((self.__graph.num_vertex, self.__graph.num_vertex))
        self.__matrixParent.fill(-1)
        self.__start = start-1 if start > 0 else 0
        self.__end = end-1 if end > 0 else 0
        self.__camino = None

#////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////
            
    @property        
    def initMatrix(self):
        for i in range(0, self.__graph.num_vertex):
            for j in range(0, self.__graph.num_vertex):
                if i == j:
                    self.__matrix[i][j] = 0
                elif self.__graph.exist_edges(i, j):
                    self.__matrix[i][j] = self.__graph.weigth_edges(i, j)
                else:
                    self.__matrix[i][j] = np.inf

#////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////
    
    @property
    def floyd_recorrido(self):
        self.initMatrix
        for k in range(0, self.__graph.num_vertex):
            for i in range(0, self.__graph.num_vertex):
                for j in range(0, self.__graph.num_vertex):
                    if self.__matrix[i][k] + self.__matrix[k][j] < self.__matrix[i][j]:
                        self.__matrix[i][j] = self.__matrix[i][k] + self.__matrix[k][j]
        self.__printPath__()
        self._paint_search_graph
        return self.__matrix
        
#////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////

    def __reconstruct_camino_mas_corto(self, distance:float):
        camino = []
        crawl = self.__end
        for i in range(0, self.__graph.num_vertex):
            for j in range(0, self.__graph.num_vertex):
                if self.__matrix[i][j] == np.inf:
                    print("INF")
                else:
                    print(self.__matrix[i][j])
                print(" ")

#/////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////

    @property
    def _paint_search_graph(self):
        camino = self.__camino
        if camino == None:
            newGraph = self.__graph.newGraph(0)   
            newGraph.paint_search_graph()
            return
        newGraph = self.__graph.newGraph(len(camino))   
        for i in range(0, len(camino)):
            newGraph.labelVertex(i, self.__graph.getLabel(camino[i]-1))
        for i in range(0, len(camino)):
            for j in range(0, len(camino)):
                if i != j:
                    newGraph.insert_edges_weigth(i, j, self.__graph.weigth_edges(camino[i]-1, camino[j]-1))
        newGraph.print_graph_labeled
        newGraph.paint_search_graph()
        return newGraph

#////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////
    '''        
    def __printPath__(self):
        distancia = self.__matrix[self.__start][self.__end]
        print("Camino minimo entre: " + str(self.__start+1) + " y " + str(self.__end+1))
        print("Distancia: " + str(distancia))
        print("Camino optimo: ", self.__reconstruct_camino_mas_corto(distancia))
        print("Cancha \t\t Distancia")
        for i in range(0, self.__graph.num_vertex):
            print(str(i+1) + " \t\t " + str(self.__matrix[self.__start][i]))
    '''


    def __printPath__(self):
        distancia = self.__matrix[self.__start][self.__end]
        camino_optimo = self.__reconstruct_camino_mas_corto(distancia)
        camino_info = []

        for i in range(0, self.__graph.num_vertex):
            camino_info.append({
                'cancha': i + 1,
                'distancia': self.__matrix[self.__start][i]
            })

        resultado = {
            'camino_minimo': {
                'inicio': self.__start + 1,
                'fin': self.__end + 1,
                'distancia': distancia,
                'camino_optimo': camino_optimo
            },
            'canchas': camino_info
        }

        return json.dumps(resultado)


#------------------------------------------------------------------------------
        
    
    
    
    
    