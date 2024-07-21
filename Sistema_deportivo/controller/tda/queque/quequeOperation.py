from controller.tda.linked.linkedList import Linked_List
from controller.exception.linkedEmpty import LinkedEmpty
class QueQueOperation(Linked_List):
    def __init__(self, top):
        super().__init__()
        self.__top= top

    @property
    def _top(self):
        return self.__top

    @_top.setter
    def _top(self, value):
        self.__top = value

    @property
    def verifyTop(self):
        print(self._lenght)
        return self._lenght <= self.__top
    
    def queque(self, data):
        if self.verifyTop:
            self.add(data, self._lenght)
        else:
            raise LinkedEmpty("Queque full")
    
    @property
    def dequeque(self):
        if self.isEmpty:
            raise LinkedEmpty("Queque empty")
        else:
            return self.delete(0)
