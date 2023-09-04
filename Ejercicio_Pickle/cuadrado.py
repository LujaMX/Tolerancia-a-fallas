class Cuadrado():
    def __init__(self):
        self.__base = 0.0
        self.__area = 0.0
    
    
    def setBase(self , base):
        self.__base = base

    def calcularArea(self):
        self.__area = self.__base * self.__base        

    def getArea(self):
        return self.__area
