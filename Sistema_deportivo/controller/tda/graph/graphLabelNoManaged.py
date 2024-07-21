from controller.exception.arrayPositionException import ArrayPositionException
from controller.tda.graph.graphLabeled import GraphLabeled
from controller.exception.arrayPositionException import ArrayPositionException
from math import nan

class GraphLabeledNoManaged(GraphLabeled):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__labels = []
        for i in range(0, num_vert):
            self.__labels.append(nan)
            
        
            
    def insert_edges_weight_E(self, label1, label2, weigth):
        v = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v != -1 and v2 != -1:
            self.insert_edges_weight(v, v2, weigth)
            self.insert_edges_weight(v2, v, weigth) 
        else:
            raise ArrayPositionException("No existen los vertices")


    '''def insert_edges_weight_E(self, label1, label2, weight):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 == -1 or v2 == -1:
            self.insert_edges_weight(label1, label2, weight)
            self.insert_edges_weight(label2, label1, weight) 
        else:
            raise ArrayPositionException("No existen los vertices")'''

    def _save_graph(self):
        self.paint_graph_labeled