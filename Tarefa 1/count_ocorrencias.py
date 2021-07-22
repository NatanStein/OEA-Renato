letras_up = 0
letras_low = 0
digitos = 0
espacos = 0
quebra_linha = 0
n_identificado = 0

nome = input("Digite o path completo do arquivo: ")

with open(nome) as arquivo:

    texto = arquivo.read()

    for letra in texto:
        if letra.isupper():
            letras_up += 1
        elif letra.islower():
            letras_low += 1
        elif letra in "0123456789":
            digitos += 1
        elif letra == " ":
            espacos += 1
        elif letra == "\t":
            espacos += 4
        elif letra == "\n":
            quebra_linha += 1
        else:
            n_identificado += 1

print('''
Letras Maiúsculas: %d
Letras Minúsculas: %d
Dígitos (0 a 9): %d
Espaço em branco: %d
Quebra de Linhas: %d
Não identificado: %d
'''%(letras_up,letras_low,digitos,espacos,quebra_linha,n_identificado)) 
