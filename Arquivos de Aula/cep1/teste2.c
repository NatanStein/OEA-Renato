#include <stdio.h>
#include <string.h>

struct S
{
    char atr1[5];
    char atr2[5];
    char atr3[5];
};

int main()
{
    struct S s;
    char* registro = "AAAAABBBBBCCCCC";
    memcpy(&s, registro, 15);
    printf("%s\n", registro);
    printf("%.5s\n", s.atr3);
    printf("%.5s\n", s.atr2);
    printf("%.5s\n", s.atr1);
    if(strncmp(s.atr1,"AAAAA",5)==0) {
        printf("É Igual\n");
    }

    if(strnstr("LALA LELE LILI","LELE",14))
    {
        printf("ACHEI\n");
    }
    else
    {
        printf("NÃO ACHEI\n");
    }

    if(strnstr("LALA LELE LILI","LOLO",14))
    {
        printf("ACHEI\n");
    }
    else
    {
        printf("NÃO ACHEI\n");
    }

    return 0;
}
