from math import pi, tan

class Poligono():
    def __init__(self):
        self.__base = 0.0
        self.__lados = 0.0
        self.__area = 0.0
    
    
    def setBase(self , base):
        self.__base = base

    def setLados(self , lados):
        self.__lados = lados

    def calcularArea(self):
        self.__area = self.__lados * self.__base**2 / (4 * tan(pi/self.__lados))        

    def getArea(self):
        return self.__area
