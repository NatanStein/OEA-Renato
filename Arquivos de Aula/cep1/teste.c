#include <stdio.h>
#include <string.h>

struct Pessoa {
    char nome[20];
    int idade;
    float peso;
};

int main()
{
    struct Pessoa p;
    FILE *f = fopen("MeusDados.dat", "wb");
//    p.nome = "Renato";
    strcpy ( p.nome , "Renato" );
    p.idade = 47;
    p.peso = 100.2;
    fwrite(&p, sizeof(p), 1, f);

    fclose(f);
}