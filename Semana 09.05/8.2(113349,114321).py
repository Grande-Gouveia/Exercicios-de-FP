#Introdução ao programa
print("Este programa irá determinar o consumo de uma viagem.")
print("Em primeiro lugar, escreve um docuemnto .txt\nNeste devem constar em cada linha: distância percorrida, litros gastos.")
print("Não insiras o valor inicial: 0,0")
ficheiro_nome = input("Por favor insere o nome do ficheiro, a acabar em .txt: ")


#Garante que o ficheiro inserido pelo utilizador está bem escrito:
if not ficheiro_nome.endswith(".txt"):
    print("\nFicheiro Inválido, um ficheiro pre-definido será usado.")
    #Criamos também uma ficheiro genérico, caso isso não se verifique:
    ficheiro_nome = "litros_genericos.txt"


#Separa o ficheiro em duas listas:
distancias = [0]
litros = [0]
with open(ficheiro_nome,"r") as file:
    lista_texto = file.read().replace("\n",",").split(",")
    #para garantir que não há entradas em branco estranhas no final 
    #(porque isso me aconteceu não sei bem porquê):
    if lista_texto[-1] == "":
        lista_texto.remove("")
    #separa a lista com todos os valores em duas listas: distancias e litros
    for i in range(0,len(lista_texto)):
        if i % 2 == 0:
            distancias.append(lista_texto[i])
        else:
            litros.append(lista_texto[i])


try:
    #Pede que trajeto o utilizador pretende usar:
    print("\nPreciso agora que seleciones o trajeto desejado.")
    baixo = int(input("Escolhe o número que servirá de inicío de trajeto\n(se selecionares 0, o trajeto começará da distancia 0): "))
    alto = int(input("Escolhe agora o número do final do trajeto: "))
    #o if é só para garantir que os números são bem inseridos
    if alto > baixo:
     distancia_percorrida = int(distancias[alto])-int(distancias[baixo])
     litros_gastos = int(litros[alto])-int(litros[baixo])
     consumo_medio = round((100 * litros_gastos) / distancia_percorrida)
     print("\nO consumo médio, por cada 100km, foi:",consumo_medio,"litros")
     print("O consumo total da viagem foi:",litros_gastos,"litros","\nE percorreste",distancia_percorrida,"km.")
    else:
        print("\nO primeiro valor que inseriste é maior que o segundo!")
except:
    print("\nOs valores dados não correspondem a linhas no documento de texto.\nTenta outra vez!")
     





