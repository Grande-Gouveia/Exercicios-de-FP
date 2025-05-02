from graphics import *

class Quadrado_rep:
   
    def __init__(self,aresta):
        """
        Cria um quadrado com a aresta indicada
        """
        self.aresta = aresta
        p1 = Point(1,1)
        p2 = Point(1 + aresta, 1 + aresta)
        quadrado = Rectangle(p1,p2)
        return quadrado

    def getRadius(self):
        """
        Returna a aresta do cubo
        """
        return self.aresta
    
    def Area(self):
        """
        Retorna a Area do quadrado
        """
        area = self.aresta * self.aresta
        return area
    
    def draw(self,win):
        """
        Desenha o quadrado
        """
        self.draw(win)

