from graphics import *

#Convertor de .jpg para .gif:
#https://ezgif.com/jpg-to-gif

#===============================
#Inicio do programa:
print("Este programa converte uma imagem em tons negativos.")
nome = input("Insere o nome da tua imagem.\n(certifica-te que é um ficheiro .gif): ")
local = input("Onde é que queres que a tua nova imagem seja guardada?: ")
janela = GraphWin("Imagem",200,200)
janela.setCoords(0,0,10,10)
#===============================
#Vê se a imagem pedida ao utilizador existe, senão usa uma alternativa:
try: 
    imagem = Image(Point(5,5), nome + ".gif")
    imagem.draw(janela)
except:
    print("\nErro! Imagem não encontrada. Uma imagem default irá ser usada.")
    imagem = Image(Point(5,5), "default.gif")
    imagem.draw(janela)
#A imagem que iria usar como default era muito grande.
#Por isso cortei-a de forma a facilitar o funcionamento do programa.
largura = int(imagem.getWidth())
altura = int(imagem.getHeight())
#===============================
#Vai transformar a imagem:
janela.getMouse()
imagem.undraw()
for i in range(largura):
    for u in range(altura):
        r = imagem.getPixel(i, u)[0]
        g = imagem.getPixel(i, u)[1]
        b = imagem.getPixel(i, u)[2]        
        inverso = color_rgb(255-r,255-g,255-b)
        imagem.setPixel(i,u,inverso)
imagem.draw(janela)
#===============================
imagem.save(local + ".gif")
janela.getMouse()
janela.close()

