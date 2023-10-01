class Transporte:
    def __init__(self,aro:float,peso:float):
        self.__aro = aro
        self.__peso = peso
        self.__costo_despacho_base = 4000

    def get_aro(self):
        return self.__aro
    def get_peso(self):
        return self.__peso

    def __str__(self):
        text = f'Aro: {self.__aro} milimetros'
        text += f'\nPeso {self.__peso} kg'
        return text