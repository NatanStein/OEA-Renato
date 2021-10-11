import struct
import time

start_time = time.time()

def intercala(a,b,t):
    contA = 0
    contB = 0
    lista_final = []
    while contA <= t and contB <= t:
        if contA >= t:
            return lista_final + b[contB:]
        else:
            listaA = a[contA]
        if contB >= t:
            return lista_final + a[contA:]
        else:
            listaB = b[contB]
        
        if listaA[5][2:] > listaB[5][2:]:
            lista_final.append(listaA)
            contA +=1
        else:
            lista_final.append(listaB)
            contB += 1
    return lista_final
        
qtt_div = 8
reg = struct.Struct("72s72s72s72s2s8s2s")

with open('cep.dat','rb') as file:
    
    tamanho_linha = reg.size
    arquivos = []
    file.seek(0,2)
    tamanho_arquivo = file.tell()
    num_linhas = int(tamanho_arquivo/tamanho_linha)
    linhas_por_arquivo = num_linhas//qtt_div
    file.seek(0,0)
    for i in range(qtt_div):
        lista = []
        for n in range(linhas_por_arquivo):
            linha = file.read(tamanho_linha)
            lista.append(reg.unpack(linha))    
        lista.sort(key=lambda e: e[5])
        arquivos.append(lista)

while len(arquivos) > 1:
    result = intercala(arquivos[0],arquivos[1],len(arquivos[0]))
    arquivos.append(result)
    arquivos.pop(0)
    arquivos.pop(0)

with open('cep_ordenado.dat','wb') as file:
    for registro in arquivos[0]:
        linha = reg.pack(*registro)
        file.write(linha)
        
print("--- %s seconds ---" % (time.time() - start_time))


