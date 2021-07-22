with open("exemplo.txt") as arquivo:
    texto = arquivo.read()
with open("exemplo_copia.txt","w") as arquivo_copia:
    arquivo_copia.write(texto)
