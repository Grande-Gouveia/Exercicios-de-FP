from graphics import *
from random import choice

janela = GraphWin("Regressão linear",500,500)
janela.setCoords(0,0,100,100)

def sistema_eixos_botao(win):
    """
    Esta função contem em si todas as componentes gráficas imóveis do programa
    """
    #Cria os eixos,textos e botao:
    texto_X = Text(Point(94,7), "X")
    texto_X.setSize(8)
    texto_Y = Text(Point(2,97), "Y")
    texto_Y.setSize(8)
    texto_0 = Text(Point(3,8), "0")
    texto_0.setSize(9)
    eixo_X = Line(Point(4,9),Point(95,9))
    eixo_X.setArrow("last")
    eixo_Y = Line(Point(4,9),Point(4,97))
    eixo_Y.setArrow("last")
    botao = Rectangle(Point(0,0),Point(16,6))
    botao.setFill("grey84")
    botao.setOutline("black")
    texto_botao = Text(Point(7,3), "Concluído")
    texto_botao.setTextColor("black")
    texto_botao.setSize(8)
    #=======================
    #Desenha as coisas acima:
    botao.draw(win)
    texto_botao.draw(win)
    texto_X.draw(win)
    texto_Y.draw(win)
    texto_0.draw(win)
    eixo_X.draw(win)
    eixo_Y.draw(win)
    #=======================

def pontos_funcao(win):
    """
    Cria os pontos e a reta
    """
    lista_x = []
    lista_y = []
    lista_cor =["blue","yellow","pink","red","green","purple","brown","orchid2","darkslategrey","gold2"]
    while True:
     ponto_desenharX = int(janela.getMouse().getX())
     ponto_desenharY = int(janela.getMouse().getY())
     #=======================
     #Este primeiro vê se o utilizador clicou no botão. Se sim, forma a reta:
     if ponto_desenharX < 16 and ponto_desenharY < 6:
         #Aqui vai definir valores para as variaveis:
         x = 0 
         y = 0
         for i in lista_x:
             x += i
         x_med = (x)/len(lista_x)
         for i in lista_y:
             y += i
         y_med = (y)/len(lista_y)
         x2 = x **2 
         xy = x * y
         m = (xy - len(lista_x) * x_med * y_med) / (x2 - len(lista_x) * (x_med)**2)
     #=======================
         #Cria a reta e o texto da equação:
         reta = Line(Point(4,y_med + m * (4 - x_med)), Point(95,y_med + m * (95 - x_med)))
         reta.setWidth(5)
         reta.setOutline("grey10")
         equacao = Text(Point(50,4), f"Reta de equação: y = {round(y_med,2)} + {round(m,2)}*(x - {round(x_med,2)})")
         equacao.setSize(10)
         reta.draw(win)
         equacao.draw(win)
         win.getMouse()
         win.close()
     #=======================
     #Este elif existe para criar os pontos:
     elif ponto_desenharX > 4 and ponto_desenharX < 95 and ponto_desenharY > 9 and ponto_desenharY < 97:
         #Se o ponto estiver dentro dos limites do grafico, ele desenha-o:
         lista_x.append(ponto_desenharX)
         lista_y.append(ponto_desenharY)
         ponto = Circle(Point(ponto_desenharX,ponto_desenharY ),1)
         cor_final = choice(lista_cor)
         ponto.setFill(cor_final)
         ponto.setOutline("black")
         ponto.draw(win)
    #=======================
     #Este else só existe para o programa ignorar quando o utilizador clica fora do gráfico e fora do botão:
     else:
         continue
    #=======================
    
sistema_eixos_botao(janela)
pontos_funcao(janela) 
