from numbers import Number
from controller.tda.linked.node import Node
from controller.exception.linkedEmpty import LinkedEmpty
from controller.exception.arrayPositionException import ArrayPositionException
from controller.tda.linked.order.mergeSort import MergeSort
from controller.tda.linked.order.shellSort import ShellSort
from controller.tda.linked.order.quickSort import QuickSort
from controller.tda.linked.search.binarySecuencial import BinarySecuencial
from controller.tda.linked.search.binary import Binary



class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0
    

    @property
    def _atype(self):
        return self.__atype

    @_atype.setter
    def _atype(self, value):
        self.__atype = value


    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value
 
        
    @property    
    def isEmpty(self):
        return self.__head == None or self._length == 0
    
    def _getFirst_(self, poss):
        if not self.isEmpty:
            return self.__head
        else:
            return "List is Empty"
    
    def _getLast_(self, poss):
        if not self.isEmpty:
            return self.__last
        else:
            return "List is Empty"
        
    def getData(self, poss):
        if self.isEmpty:
           raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            return self.__head._data
        elif poss == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < poss:
                cont += 1
                node = node._next
            return node._data
        

    def getNode(self, poss):
        if self.isEmpty:
           raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            return self.__head
        elif poss == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < poss:
                cont += 1
                node = node._next
            return node
            
    def add(self, data, pos = 0):
        if pos == 0:
            self.addFirst(data)
        elif pos == self.__length:            
            self.addLast(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next#self.getNode(pos) 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
            
                
    def addFirst(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length += 1
        else:
            headOld = self.__head #guarada toda la lista hara ahora
            node = Node(data, headOld)  
            self.__head = node
            self.__length += 1

    def addLast(self, data):
        if self.isEmpty:
            self.addFirst(data)
        else:
            node = Node(data)
            self.__last._next = node 
            self.__last = node
            self.__length += 1

    def get(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data
        
        
    def addNode(self, data, pos = 0):
        if pos == 0:
            self.addFirst(data)
        elif pos == self.__length:            
            self.addLast(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1


    def edit (self, data, poss = 0):
        if poss == 0:
            print("entro en 0 en edit")
            print(data)
            self.__head._data = data
        elif poss == (self.__length - 1):
            self.__last._data = data
        else:
            node = self.getNode(poss)
            node._data = data

    def delete(self, pos):
        pos = pos 
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Position is out of range")
        elif pos == 0:
            self.__head = self.__head._next
            self.__length -= 1
            
        elif pos == self._length -1:
            self.__last = self.getNode(pos-1)
            #restarId
            self.__length -= 1
        else:
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next._next
            node_preview._next = node_last
            self.__length -= 1
            
        for i in range(pos, self._length):
            self.getNode(i)._data._id = i+1
   
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0  
   
    @property
    def toArray(self):
        #TODO
        #array = TDAArray(self.__length)
        array = []               
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self._length:
                array.append(node._data)
                #array.insert(node._data, cont)
                cont += 1
                node = node._next
        return array
    
    @property
    def to_dict(self):
        data = []
        node = self.__head
        while node != None:
            data.append(node._data)
            node = node._next
        return data
    
    def serializable(self):
        data = []
        node = self.__head
        while node != None:
            data.append(node._data)
            node = node._next
        return data
    
    def deserializar(data):
        linked = Linked_List()
        for i in data:
            linked.addNode(i)
        return linked
    
    @property
    def serializable(self):
        array = self.toArray 
        array_dict = []
        for i in range(0, len(array)): 
            array_dict.append(array[i].serializable) 
        return array_dict
    

    @classmethod
    def deserializar(self, array_dict):
        linked = Linked_List()
        linked.dicToListLast(array_dict)
        return linked
    
    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.addLast(array[i])        

    def __str__(self) -> str: #metodo toString    #cometar ctrl+k+c   / ctrl+k+u
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data) + " -> "
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node != None :
            data += str(node._data) + "   "
            node = node._next
        print("Lista de datos")
        print(data)
    # -------------------------------------------Metodos de Ordenacion-------------------------------------------------------------
    
    def sort(self, type, typeSort = 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], Number) or isinstance(array[0], str):
                if typeSort == 1:
                    order = QuickSort()
                elif typeSort == 2:
                    order = MergeSort()
                else:
                    order = ShellSort()
                if type == 1:
                    array = order.sort_primitive_ascendent(array)
                else:
                    array = order.sort_primitive_descendent(array)
            self.toList(array)

    def sort_models(self, attribute, type = 1, typeSort = 1):
            if self.isEmpty:
                raise LinkedEmpty("List empty")
            else:
                array = self.toArray
                if isinstance(array[0], object):
                    if typeSort == 1:
                        order = QuickSort()
                    elif typeSort == 2:
                        order = MergeSort()
                    else:
                        order = ShellSort()
                    if type == 1:
                        array = order.sort_models_ascendent(array, attribute)
                    else:
                        array = order.sort_models_descendent(array, attribute)
                self.toList(array)
            return self
    # -------------------------------------------Metodos de Busqueda-------------------------------------------------------------

    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            for i in range (0, len(array)):
                if (array[i].lower().__contains__(data.lower())):    
                    list.add(array[i], list._length)
        return list
    
    def binary_search(self, data, type = 1):
        array = self.toArray
        order = QuickSort()
        array = order.sort_primitive_ascendent(array)
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            search = Binary()
            if type == 0:
                return search.binary_string(array, data, 0, len(array) - 1)
            elif type == 1:
                return search.binary_primitive(array, data, 0, len(array) - 1)  
            
                
    def binary_search_models(self, data, attribute, type=1):
        array = self.toArray
        order = ShellSort()
        array = order.sort_models_ascendent(array, attribute)
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            search = Binary()
            result = None
            if type == 1:
                result = search.search_models(array, data, attribute, 0, len(array) - 1)
            elif type == 2:
                result = search.search_models(array, data, attribute, 0, len(array) - 1)
                print(attribute)
            return result

    def binary_models(self, data, attribute, type=1):
        array = self.toArray
        order = QuickSort()
        array = order.sort_models_ascendent(array, attribute)
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            search = BinarySecuencial()
            if type == 1:
                result = search.binary_models_secuencial(array, data, 0, len(array) - 1, attribute)
                return result
