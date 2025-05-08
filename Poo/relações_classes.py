class Carro:
    def __init__(self, modelo, motor, fabricante):
        self.__modelo = modelo
        self.__motor = motor
        self.__fabricante = fabricante

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor  
    
    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, valor):
        self.__motor = valor
    
    @property
    def fabricante(self):  
        return self.__fabricante
    
    @fabricante.setter  
    def fabricante(self, valor):
        self.__fabricante = valor

class Motor:
    def __init__(self, nome):
        self.__nome = nome
        self.__estado = "desligado"

    @property
    def nome(self):
        return self.__nome
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, valor):
        self.__estado = valor
    
v8 = Motor("V8")
carro = Carro("Kiwd", v8, None)


print(carro.motor.nome)