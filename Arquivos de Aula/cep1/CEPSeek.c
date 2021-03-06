#include <stdio.h>

typedef struct _Endereco Endereco;

struct _Endereco
{
	char logradouro[72];
	char bairro[72];
	char cidade[72];
	char uf[72];
	char sigla[2];
	char cep[8];
	char lixo[2];
};

//	fseek(f,0,SEEK_END);
// 	fseek(f,0,SEEK_CUR);
//  fseek(f,0,SEEK_SET);

int main(int argc, char**argv)
{
	FILE *f;
	Endereco e;
	int qt;
	long tamanhoArquivo, posicao, primeiro, ultimo, meio;

	if(argc != 2)
	{
		fprintf(stderr, "USO: %s [CEP]", argv[0]);
		return 1;
	}
	f = fopen("cep_ordenado.dat","r");
	fseek(f,0,SEEK_END);
	tamanhoArquivo = ftell(f);
	rewind(f); // fseek(f,0,SEEK_SET);
	printf("Tamanho do Arquivo: %ld\n", tamanhoArquivo);
	printf("Tamanho do Registro: %ld\n", sizeof(Endereco));
	printf("Tamanho do Arquivo em Registros: %ld\n", tamanhoArquivo/sizeof(Endereco));
	primeiro = 0;
	ultimo = (tamanhoArquivo/sizeof(Endereco))-1;
	meio = (primeiro+ultimo)/2;
	fread(&e,sizeof(Endereco),1,f);
	printf("PRIMEIRO:\n%.72s\n%.72s\n%.72s\n%.72s\n%.2s\n%.8s\n",e.logradouro,e.bairro,e.cidade,e.uf,e.sigla,e.cep);
	printf("Posicao Atual: %ld\n", ftell(f));
	fseek(f, meio * sizeof(Endereco), SEEK_SET);	
	printf("Posicao Atual: %ld\n", ftell(f));
	fread(&e,sizeof(Endereco),1,f);
	printf("MEIO:\n%.72s\n%.72s\n%.72s\n%.72s\n%.2s\n%.8s\n",e.logradouro,e.bairro,e.cidade,e.uf,e.sigla,e.cep);
	printf("Posicao Atual: %ld\n", ftell(f));
	fseek(f, ultimo * sizeof(Endereco), SEEK_SET);	
	printf("Posicao Atual: %ld\n", ftell(f));
	fread(&e,sizeof(Endereco),1,f);
	printf("ULTIMO:\n%.72s\n%.72s\n%.72s\n%.72s\n%.2s\n%.8s\n",e.logradouro,e.bairro,e.cidade,e.uf,e.sigla,e.cep);
	printf("Posicao Atual: %ld\n", ftell(f));
	fclose(f);
	return 0;
}

