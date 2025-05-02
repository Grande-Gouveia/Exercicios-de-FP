from graphics import *

class Esfera_rep:
    def __init__(self,radius):
        """
        Cria uma esfera com o raio indicado
        """
        self.radius = radius
        circulo = Circle(Point(5,5), radius)
        return circulo
    
    def getRadius(self):
        """
        Retorna o raio da esfera.
        """
        return self.radius
    
    def surfaceArea(self):
        """
        Retorna a Area de superficie da esfera.

        """
        area = int(4 * 3.14159 * (self.radius)**2)
        return area
    
    def volume(self):
        """
        Retorna o volume da esfera.
        """
        volume = (4/3) * 3.14159 * (self.radius)**3
        return volume
