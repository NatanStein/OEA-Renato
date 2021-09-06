import struct
import re

reg = struct.Struct("72s72s72s72s2s8s2s")
query = input("Digite o CEP para ser buscado: ")
achou = False

with open('Tarefa 5\\cep_ordenado.dat','rb') as file:
    
    tamanho_linha = reg.size
    
    file.seek(0,2)
    tamanho_arquivo = file.tell()
    num_linhas = int(tamanho_arquivo/tamanho_linha)

    fim = (num_linhas)
    inicio = 0
    cont = 0
    while inicio <= fim:
        cont+=1
        meio = (inicio+fim)//2
        file.seek(meio*tamanho_linha,0)
        linha = file.read(tamanho_linha)
        local = reg.unpack(linha)
        cep = local[-2].decode()
        if query == cep:
            achou = True
            break
        elif query > cep:
            inicio = meio + 1
        else:
            fim = meio - 1
if achou:

    rua = re.sub('  +', '',local[0].decode('latin-1'))
    bairro = re.sub('  +', '',local[1].decode('latin-1'))
    cidade = re.sub('  +', '',local[2].decode('latin-1'))
    estado = re.sub('  +', '',local[3].decode('latin-1'))
    cep = re.sub('  +', '',local[4].decode('latin-1')) + re.sub('  +', '',local[5].decode('latin-1')) 

    print(f"""
    Rua: {rua} 
    Bairro: {bairro} 
    Cidade: {cidade} 
    Estado: {estado} 
    CEP: {cep}
    """)
else:
    print(f"CEP {query} não foi encontrado!")