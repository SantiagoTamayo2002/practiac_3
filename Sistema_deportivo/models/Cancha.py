class Canchas():
    def __init__(self) -> None:
        self.__id = 0
        self.__nombre = ""
        self.__direccion = 's/n'
        self.__precio = 's/n'
        self.__lng = '0.0'
        self.__lat = '0.0'


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _precio(self):
        return self.__precio
    
    @_precio.setter
    def _precio(self, value):
        self.__precio = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _lng(self):
        return self.__lng

    @_lng.setter
    def _lng(self, value):
        self.__lng = value

    @property
    def _lat(self):
        return self.__lat

    @_lat.setter
    def _lat(self, value):
        self.__lat = value

    @property    
    def serializable(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "direccion": self.__direccion,
            "precio": self.__precio,
            "lng": self.__lng,
            "lat": self.__lat
        }
    
    def deserializar(data):
        negocio = Canchas()
        negocio._id = data["id"]
        negocio._nombre = data["nombre"]
        negocio._direccion = data["direccion"]
        negocio._precio = data["precio"]
        negocio._lng = data["lng"]
        negocio._lat = data["lat"]
        return negocio

    def __str__(self) -> str:
        return f"{self.__id} {self.__nombre} {self.__direccion} {self.__precio} {self.__lng} {self.__lat}"