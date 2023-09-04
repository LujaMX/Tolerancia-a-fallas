class Rectangulo():
    def __init__(self):
        self.__base = 0.0
        self.__altura = 0.0
        self.__area = 0.0
    
    
    def setBase(self , base):
        self.__base = base

    def setAltura(self , altura):
        self.__altura = altura

    def calcularArea(self):
        self.__area = self.__base * self.__altura        

    def getArea(self):
        return self.__area
