import sys
import os , json
import geopy.distance
from math import sin, cos, sqrt, atan2, radians, asin

class Graph:


    def __init__(self):
        self.__URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath(__file__))))))

    @property
    def num_vertex(self):
        raise NotImplementedError("Please implement this method")
    
    @property
    def num_edges(self):
        raise NotImplementedError("Please implement this method")
    
    def exist_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def weigth_edges(self, v1,v2):
        print("es este?")
        raise NotImplementedError("Please implement this method")
    
    def insert_edges_weigth(self, v1, v2, weigth):
        print("ayudaadaa")
        raise NotImplementedError("Please implement this method")
    
    def insert_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def adjacent(v1):
        raise NotImplementedError("Please implement this method")
    
    def getLabel(self, vertex):
        raise NotImplementedError("Please implement this method")
    
    def getVertex(self, label):
        raise NotImplementedError("Please implement this method")
    
    def newGraph(self, num_vertex):
        print("holaaaa")
        raise NotImplementedError("Please implement this method")
    
    def paint_search_graph(self,nameComponent='mynetworkSearch', file="grafoSearch.js"):
        self.paint_graph_labeled(file=file, nameComponent=nameComponent, mostrarCamino=True)

#///////////////////////////////////////////////////////////////////////////////////////////////////
    
    def archivo_buscar(self, file):
        url = self.__URL +'/data/'+file
        return os.path.exists(url)
    

    def __str__(self) -> str:
        out = []
        for i in range(self.num_vertex):
            out.append(f"V{i} ->")
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(adjs._length):
                    adj = adjs.get(j)
                    out.append(f"  ady V{adj._destination + 1} weigth {adj._weigth}")
        return "\n".join(out)
    
    '''
    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i) + " -> "
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"   
        return out
    '''

    
    @property
    def paint_graph(self, file='d3/grafo.js'):
        url = self.__URL +'/static/'+ file
        print(url)
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js+= '\n{id:'+str(i+1)+', label: "'+str(i+1)+'"},'
        js = js[:-1]
        js += ']);\n'
    
        js+= '\n var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    js += '{\nfrom: '+str(i+1)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
        a = open(url , 'w')
        a.write(js)
        a.close()
        
    def paint_graph_labeled(self, file='grafo.js', nameComponent="mynetwork" ,mostrarCamino = False):
        url = self.__URL +'/static/d3/'+ file
        camino = ""
        weigths = []
        if self.num_vertex == 0:
            js = 'var advertencia = document.getElementById("advertencia");\n'
            js+= 'advertencia.innerHTML = "No hay datos en los caminos para poder llegar al destino";'
            a = open(url , 'w')
            a.write(js)
            a.close()
            return
        
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js+= '\n{id:'+str(i)+', label: "'+str(self.getLabel(i))+'"},'
            camino += ' '+str(self.getLabel(i))+' => '
        js = js[:-1]
        js += ']);\n'
        
        js+= '\n var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    if adj._weigth != None and adj._destination != None:
                        weigths.append(adj._weigth) if adj._weigth not in weigths else weigths
                        js += '{\nfrom: '+str(i)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("'+nameComponent+'"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
        if mostrarCamino:
            js += 'var camino = document.getElementById("camino");\n camino.innerHTML = "'+camino[:-3]+'";'
            js += 'var weigths = document.getElementById("weigths");\n weigths.innerHTML = "'+str(sum(weigths))+'";'
        a = open(url , 'w')
        a.write(js)
        a.close()
        
    @property
    def print_graph(self):
        print(self.__str__())
        
    @property
    def print_graph_labeled(self):
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i) + " -> " + str(self.getLabel(i)) + " -> "
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"
        print(out)


    

    def __transform_graphLabeled__(self):
        json = "["
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            json += '\n\t{\n\t\t"labelId":' + f"{str(self.getVertex(self.getLabel(i))+1)},"
            #json += '\n\t\t"label": "' + str(self.getLabel(i)) + '",'
            if not adjs.isEmpty:
                json += '\n\t\t"destinations": ['
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    json += '\n\t\t\t{\n\t\t\t\t"from":'+f"{str(self.getVertex(self.getLabel(i))+1)}"+', \n\t\t\t\t"to":'+str(adj._destination+1)+'\n\t\t\t},'
                json = json[:-1]
                json += '\n\t\t]'
                json += '\n\t},'
            else:
                json += '\n\t\t"destinations": []\n'
                json = json[:-1]
                json +='\n\t},'
            adjs = self.adjacent(i)
        json = json[:-1]
        json += "\n]"
        
        return json
    
    def save_graph_labeled(self, file='grafo.json'):
        url = self.__URL +'/data/'+file
        a = open(url , 'w')
        a.write(self.__transform_graphLabeled__())
        a.close()
        
    
    

#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////
    '''
    def reconstruir_graph(self, file='grafo.json', atype: object = None, model: object = None):
        url = f"{self.__URL}/data/{file}"
        with open(url, 'r') as f:
            data = json.load(f) 
        newGraph = atype
        newModel = model()._lista
        modelos = [newModel.get(item['labelId'] - 1) for item in data]
        for i, item in enumerate(data):
            newGraph.labelVertex(item['labelId'] - 1, modelos[i])
        for item in data:
            for dest in item['destinations']:
                distancia = (modelos[dest['from'] - 1], modelos[dest['to'] - 1])
                newGraph.insert_edges_weigth(dest['from'] - 1, dest['to'] - 1, distancia)
        return newGraph
    '''
    
    def reconstruir_graph(self, file='grafo.json', atype: object = None, model: object=None):
        url = self.__URL +'/data/'+file
        a = open(url , 'r')
        data = json.load(a)
        a.close()
        newGraph = atype
        newModel = model()._lista
    
        modelos = []      
        for item in data:
            model = newModel.get(item['labelId']-1)
            newGraph.labelVertex(item['labelId']-1,model)
            modelos.append(model)
        
        for item in data:
            destination = item['destinations']
            if destination != []:
                for dest in item['destinations']:
                    distacia = calcular_distancias(modelos[dest['from']-1], modelos[dest['to']-1])
                    newGraph.insert_edges_weigth(dest['from']-1, dest['to']-1, distacia)
        return newGraph


#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////
    
    def obtain_weigths(self, graph:object =None, file='grafo.json'):
        print(graph)
        out = []
        for i in range(0, graph.num_vertex):
            info = {}
            adjs = graph.adjacent(i)
            if not adjs.isEmpty:
                info['labelId'] = graph.getVertex(graph.getLabel(i))+1
                info['destinations'] = []
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    info['destinations'].append({
                        'from': graph.getVertex(graph.getLabel(i))+1,
                        'to': adj._destination+1,
                        'weigth': adj._weigth
                    })
                out.append(info)
        return out
            
#///////////////////////////////////////////////////////////////////////////////////////////////////

def calcular_distancias(model1: object = None, model2: object = None):
    R = 6371.01
    lat1 = model1._latitud
    lon1 = model1._longitud
    lat2 = model2._latitud
    lon2 = model2._longitud
    distancia = geopy.distance.distance((lat1, lon1), (lat2, lon2)).km
    return round(distancia,2)

#///////////////////////////////////////////////////////////////////////////////////////////////////
            
        