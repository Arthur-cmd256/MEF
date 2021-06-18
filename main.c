#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define Acordado 1
#define Trabalhando 2
#define Descansando 3
#define Dormindo 4
#define h8 8
#define h9 9
#define h12 12
#define h13 13
#define h18 18
#define h22 22

void Converte(int resultado)
{  
    switch (resultado)
    {
    case 1:
        printf("Acordado");
        break;
    case 2:
        printf("Trabalhando");
        break;
    case 3:
        printf("Descansando");
        break;
    case 4:
        printf("Dormindo");
        break;
    case 8:
        printf("8 horas");
        break;
    case 9:
        printf("9 horas");
        break;
    case 12:
        printf("12 horas");
        break;    
    case 13:
        printf("13 horas");
        break;
    case 18:
        printf("18 horas");
        break;
    case 22:
        printf("22 horas");
        break;
    
    default:
        break;
    }
    
}

int main()
{   int entrada, EstadoAtual, TransicaoAtual, c=0, l, cont=1;
    int relacionamento[6][3] = {{Dormindo, h8, Acordado},
                                {Acordado, h9, Trabalhando},
                                {Trabalhando, h12, Descansando},
                                {Descansando, h13, Trabalhando},
                                {Trabalhando, h18, Descansando},
                                {Descansando, h22, Dormindo}};
    
        printf("|-|-|-|  MAQUINA DE ESTADOS FINITA  |-|-|-|\n");
        printf("\nDigite 1 para entrada de um Estado");
        printf("\nDigite 2 para entrada de uma Transicao\n\n");
        scanf("%d", &entrada);
        if(entrada == 1){
            printf("\nEscolha uma dessas opcoes de Estados abaixo: \n\n");
            printf("Digite 1 para Acordado\n");
            printf("Digite 2 para Trabalhando\n");
            printf("Digite 3 para Descansando\n");
            printf("Digite 4 para Dormindo\n\n");
            scanf("%d", &EstadoAtual);

            for ( l=0; l <= 6; l++)
            {   
                c=0;
                if (EstadoAtual == relacionamento[l][c] && cont == 1)
                {   
                    c=1;
                    printf("\nA proxima Transicao possivel sera ");
                    Converte(relacionamento[l][c]);
                    cont++;
                }
                if (EstadoAtual == relacionamento[l][c] && cont > 1)
                {   
                    c=1;
                    printf(" ou as ");
                    Converte(relacionamento[l][c]);
                    cont++;
                }
            }
            
        }
        else if(entrada == 2){
            printf("\nEscolha uma dessas opcoes de Transições abaixo: \n\n");
            printf("Digite 8 para 8h\n");
            printf("Digite 9 para 9h\n");
            printf("Digite 12 para 12h\n");
            printf("Digite 13 para 13h\n");
            printf("Digite 18 para 18h\n");
            printf("Digite 22 para 22h\n\n");
            scanf("%d", &TransicaoAtual);
            for ( l=0; l <= 6; l++)
            {   c=1;  
                if (TransicaoAtual == relacionamento[l][c])
                {   
                    c=2;
                    printf("\nA maquina se encontra no estado ");
                    Converte(relacionamento[l][c]);    
                }
            }
        }
    return 0;
}


