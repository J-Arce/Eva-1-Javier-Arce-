from Transporte import Transporte
class Bicicleta(Transporte):
    def __init__(self,aro:float,peso:float,precio:float,marca:str):
        super().__init__(aro,peso)
        self.__precio = precio
        self.__marca = marca
        self.__despacho = None
    
    def get_precio(self):
        return self.__precio
    def get_marca(self):
        return self.__marca
    def get_despacho(self):
        return self.__despacho

    def calcular_despacho(self):
        self.__despacho = self._Transporte__costo_despacho_base + 400 * self.get_peso()
    
    def __str__(self):
        text = super().__str__()
        text += f'\nPrecio: ${self.__precio}'
        text += f'\nMarca: {self.__marca}'
        text += f'\nCosto despacho: ${self.__despacho}'
        text += f'\nCosto total: ${self.__precio + self.__despacho}\n'
        return text