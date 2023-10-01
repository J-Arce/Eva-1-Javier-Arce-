from Tecnologia import Tecnologia
class Consola(Tecnologia):
    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str,nombre_consola:str,version:str):
        super().__init__(voltaje,precio,eficiencia,marca)
        self.__nombre_consola = nombre_consola
        self.__version = version
        self._Tecnologia__descuento = 1
        self._Tecnologia__nuevo_precio = self._Tecnologia__precio

    def get_nombre_consola(self):
        return self.__nombre_consola
    def get_version(self):
        return self.__version

    def calcular_descuento(self):
        super().calcular_descuento()
        if self.__version == 'Lite':
            self._Tecnologia__descuento += 0.05
        self._Tecnologia__nuevo_precio = self._Tecnologia__precio * (1 - self._Tecnologia__descuento)

    def __str__(self):
        text = super().__str__()
        text += f'Nombre: {self.__nombre_consola}'
        text += f'\nVersion: {self.__version}'
        return text





