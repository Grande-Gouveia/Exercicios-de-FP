
def QuadradoElementos(numeros : list) -> list:
    """
    De uma lista com numeros, a função retorna uma lista 
    com os numeros todos ao quadrado.
    """
    numeros_quadrados = []
    for i in numeros:
        a = i**2
        numeros_quadrados.append(a)
    return numeros_quadrados

def SomatorioLista(numeros: list) -> int:
    """
    De uma lista com numeros, retorna a soma destes.
    """
    soma = 0
    for i in numeros:
        soma += i 
    return soma

def ConverteEmNumeros(ListaCaracteres: list) -> list:
    """
    De uma lista com strings que serão números, 
    Transforma cada um num float.
    """
    lista_indexs = []
    for i in range(0,len(ListaCaracteres)):
        a = float(ListaCaracteres[i])
        lista_indexs.append(a)
    return lista_indexs



def main():
    """
    Função main 
    """
    print("O seguinte programa transforma os numeros de um ficheiro.")
    while True:
        nome = input("Qual é o nome do teu ficheiro? ")
        try:
            #pode usar o documento deafult: numeros.txt
            with open(nome,"r") as file:
                a = file.readlines()
                b = []
                for i in a:
                    num = i.strip("\n")
                    b.append(num)
                c = SomatorioLista(QuadradoElementos(ConverteEmNumeros(b)))
            print("\nA soma dos quadrados dos numeros do teu ficheiro é:", c)
            break
        except:
            print("\nNome de ficheiro incorreto!!\nMeteste o .txt?\n")
   
main()        

  

    
   
    
   
    
   