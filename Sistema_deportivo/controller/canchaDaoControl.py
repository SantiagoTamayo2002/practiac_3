from controller.dao.daoAdapter import DaoAdapter
from models.Cancha import Canchas


class CanchaDaoControl(DaoAdapter):
    def __init__(self, atype = any):
        super().__init__(Canchas)
        self.__cancha = None


    @property
    def _negocio(self):
        if self.__cancha == None:
            self.__cancha = Canchas()
        return self.__cancha


    @_negocio.setter
    def _negocio(self, value):
        self.__cancha =value


    @property
    def _lista(self):
        return self._list()

    @property
    def save(self):
        self._save(self._negocio)

    '''
    @property    # agregar una lista de adyacencia para cada cancha
    def save(self):
        lista = self._lista()
        self.__cancha._id = lista._length + 1
        self._save(self.__cancha)
    '''
    
    def merge(self, pos):
        self._merge(self.__cancha, pos)
        
    
    def delete(self, pos):
        self._delete(self.__cancha, pos)



