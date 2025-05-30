print("O seguinte programa verifica se uma data é válida.")
print("Por favor não insiras os dias e os meses com um zero, assim: 01")
data = input("Insere uma data no formato dia/mês/ano : ")

meses_com_31 = [1,3,5,7,8,10,12]
meses_com_30 = [4,6,9,11]

try:
    data_separada = data.split("/")
    dia = int(data_separada[0])
    mes = int(data_separada[1])
    ano = int(data_separada[2])
    dia_bool = None
    mes_bool = None
    #=================
    #Assegura que os dias estão certos:
    if dia == 31:
        if mes in meses_com_31:
            print("Dia válido.")
            dia_bool = True
        elif mes in meses_com_30:
            print("O mês inserido não tem 31 dias.")
            dia_bool = False
        elif mes == "02" or mes == "2":
            print("Fevereiro não tem 31 dias.")
            dia_bool = False
            mes_bool = False
        else:
            pass
    elif dia == 30:
        if mes in meses_com_30:
            print("Dia válido.")
            dia_bool = True
        elif mes in meses_com_31:
            print("O mês inserido não tem 30 dias.")
            dia_bool = False
        elif  mes == 2:
            print("Fevereiro não tem 30 dias.")
            dia_bool = False
        else:
            pass
    elif dia == 29 and mes == 2:
        print("Fevereiro não tem 29 dias.")
        mes_bool = False
    elif dia > 31:
        print("Dia inválido.")
        dia_bool = False
    else:
        print("Dia válido.")
            
    #=================
    #Assegura o mes:
    if mes >= 13 or mes <= 0:
        print("Mês inválido.")
        mes_bool = False 
    else:
        print("Mês válido.")
        mes_bool = True
    #=================
    #Mensagem final:
    if mes_bool == True and dia_bool == True:
        print("\nData válida.")
    else:
        print("\nData inválida.")   
except:
    print("\nData inserida possui um formato não válido!")



