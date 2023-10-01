from Tecnologia import Tecnologia
from Transporte import Transporte
class Scooter(Tecnologia,Transporte):
    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str,aro:float,peso:float,velocidad:int):
        Tecnologia.__init__(self,voltaje,precio,eficiencia,marca)
        Transporte.__init__(self,aro,peso)
        self.__velocidad = velocidad
        self.__despacho = None

    def get_velocidad(self):
        return self.__velocidad
    def get_despacho(self):
        return self.__despacho
    
    def calcular_despacho(self):
        self.__despacho = self._Transporte__costo_despacho_base + 300 * self.get_peso()

    def __str__(self):
        text = Tecnologia.__str__(self)
        text += Transporte.__str__(self)
        text += f'\nVelocidad: {self.__velocidad} km/h'
        text += f'\nCosto despacho: ${self.__despacho}'
        text += f'\nCosto total: ${self.get_nuevo_precio() + self.__despacho}\n'
        return text