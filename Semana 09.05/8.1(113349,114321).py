from graphics import *

class GrupoGrafico:
    def __init__(self,ancora):
        """
        Função que cria o ponto ancora e contem a lista/grupo com todos os objetos
       
        """
        self.ancora = ancora
        self.grupo = []
        
    def retornaAncora(self):
        """
       Retorna um ponto ancora clonado

        """
        return self.ancora
    
    def AdicionaObjeto(self,objeto):
        """
        Adiciona um objeto à lista/grupo
        """
        self.grupo.append(objeto)
        
    def move(self,dx,dy,ancora):
        """
        Move dx e dy cordenadas todos os objetos do grupo e o ponto ancora

        """
        for i in self.grupo:
            i.move(dx,dy)
        self.ancora.move(dx,dy)
        
    def desenha(self,win):
        """
        Desenha todos os objetos no grupo, nunca o ponto ancora

        """
        for i in self.grupo:
            i.draw(win)
            
    def apaga(self):
        """
        Apaga todos os desenhos presentes no grupo
        """
        for i in self.grupo:
            i.undraw()
       
#=============================================================================

janela = GraphWin("O objeto movél",800,800)
janela.setCoords(0,0,200,200)

def coisa(win,x,y):
    #Define um objeto qualquer:
    grupo_coisa = GrupoGrafico(Point(x,y))
    ancoraX = grupo_coisa.retornaAncora().getX()
    ancoraY = grupo_coisa.retornaAncora().getY()
    #===========================
    circulo = Circle(Point(ancoraX,ancoraY),60)
    circulo.setFill("pink")
    grupo_coisa.AdicionaObjeto(circulo)
    #===========================
    bola = Circle(Point(ancoraX - 20,ancoraY +30),20)
    ret = Rectangle(Point(ancoraX + 10,ancoraY + 10),Point(ancoraX + 30,ancoraY + 30))
    bola.setFill("red")
    ret.setFill("blue")
    grupo_coisa.AdicionaObjeto(bola)
    grupo_coisa.AdicionaObjeto(ret)
    #===========================
    oval = Oval(Point(ancoraX -40,ancoraY - 20),Point(ancoraX -10,ancoraY))
    oval.setFill("green")
    grupo_coisa.AdicionaObjeto(oval)
    #===========================
    grupo_coisa.desenha(win)
    return grupo_coisa

    
x = coisa(janela,50,50)

while True:
    #Recebe o ponto do utilizador, apaga o desenho criado anteriormente 
    #e desenha o mesmo desenho com as novas coordenadas:
    ponto_movimentoX = janela.getMouse().getX()
    ponto_movimentoY = janela.getMouse().getY()
    x.apaga()
    x = coisa(janela,ponto_movimentoX,ponto_movimentoY)
    
    
   




