class Tecnologia:
    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca
        self.__descuento = None
        self.__nuevo_precio = None

    def get_voltaje(self):
        return self.__voltaje
    def get_precio(self):
        return self.__precio
    def get_eficiencia(self):
        return self.__eficiencia
    def get_marca(self):
        return self.__marca
    def get_descuento(self):
        return self.__descuento
    def get_nuevo_precio(self):
        return self.__nuevo_precio

    def calcular_descuento(self):
        if self.get_eficiencia().upper() == 'A' or self.get_eficiencia().upper() == 'B':
            self.__descuento = 0.5
        elif self.get_eficiencia().upper() == 'C' or self.get_eficiencia().upper() == 'D':
            self.__descuento = 0.3
        elif self.get_eficiencia().upper() == 'E' or self.get_eficiencia().upper() == 'F':
            self.__descuento = 0.1
        else:
            self.__descuento = 0
        self.__nuevo_precio = self.__precio * (1 - self.__descuento)
    
    def __str__(self):
        text = f'Voltaje: {self.__voltaje}V'
        text += f'\nPrecio: ${self.__precio}'
        text += f'\nEficiencia: {self.__eficiencia.upper()}'
        text += f'\nMarca: {self.__marca}\n'
        if self.__descuento is not None:
            text += f'\nDescuento aplicado: {self.__descuento * 100}%'
        if self.__nuevo_precio is not None:
            text += f'\nPrecio con descuento: ${self.__nuevo_precio}\n'
        return text