import math
from controller.canchaDaoControl import CanchaDaoControl
from controller.tda.graph.graphLabelNoManaged import GraphLabeledNoManaged

class NegocioGrafo:
    def __init__(self):
        self.__grafo = None
        self.__canchaDao = CanchaDaoControl()
        self.__dirPhysical = "static/d3/grafo.js"



    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        r = 6371
        return c * r


    def create_graph(self):
        list = self.__canchaDao._lista
        if list._length > 0:
            self.__grafo = GraphLabeledNoManaged(list._length)
            array = list.toArray
            for i in range(len(array)):
                self.__grafo.labelVertex(i, array[i]._nombre)
            for i in range(len(array)):
                for j in range(i + 1, len(array)):
                    lat1 = float(array[i]._lat)
                    lon1 = float(array[i]._lng)
                    lat2 = float(array[j]._lat)
                    lon2 = float(array[j]._lng)
                    distance = self.haversine(lat1, lon1, lat2, lon2)
                    self.__grafo.insert_edges_weight_E(array[i]._nombre, array[j]._nombre, distance)
            self._save_graph_file(array)



    def _save_graph_file(self, array): # <-- Con esta escribo en el archivo js para no perder la informacion
        nodes = [{"id": i + 1, "label": array[i]._nombre} for i in range(len(array))]
        edges = []
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                lat1 = float(array[i]._lat)
                lon1 = float(array[i]._lng)
                lat2 = float(array[j]._lat)
                lon2 = float(array[j]._lng)
                distance = self.haversine(lat1, lon1, lat2, lon2)
                edges.append({"from": i + 1, "to": j + 1, "label": f'{distance:.2f} km', "length": distance * 1000})
        graph_js_content = f"""
        var nodes = new vis.DataSet({nodes});
        var edges = new vis.DataSet({edges});
        var container = document.getElementById("mynetwork");
        var data = {{ nodes: nodes, edges: edges }};
        var options = {{}};
        var network = new vis.Network(container, data, options);
        """
        with open(self.__dirPhysical, 'w') as file:
            file.write(graph_js_content)
