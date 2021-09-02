import re
import math
intervalo = 72
query = 99074570
with open('cep_ordenado.dat') as file:
    
    tamanho_linha = len(file.readline())
    
    file.seek(0,2)
    tamanho_arquivo = file.tell()
    num_linhas = int(tamanho_arquivo/300)

    fim = (num_linhas-1)
    inicio = 0
    cont = 0
    while inicio <= fim:
        cont+=1
        meio = (inicio+fim)//2
        file.seek(meio*tamanho_linha,0)
        linha = file.readline()
        cep = int(linha[intervalo*4:].strip()[2:])
        print(cep,inicio,meio,fim)
        if query == cep:
            linha = linha[:intervalo*4]
            linha = re.sub('  +', ';',linha)
            local = linha.split(";")
        elif query > cep:
            inicio = meio + 1
        else:
            fim = meio - 1

 