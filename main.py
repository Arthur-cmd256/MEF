# Essa função converte
def converte(resultado):
    if resultado == 1:
        print("Acordado")
    elif resultado == 2:
        print("Trabalhando")
    elif resultado == 3:
        print("Descansando")
    elif resultado == 4:
        print("Dormindo")
    elif resultado == 8:
        print("8 horas")
    elif resultado == 9:
        print("9 Horas")
    elif resultado == 12:
        print("12 horas")
    elif resultado == 18:
        print("18 horas")
    elif resultado == 22:
        print("22 Horas")


relacionamento = [[4, 8, 1],
                  [1, 9, 2],
                  [2, 12, 3],
                  [3, 13, 2],
                  [2, 18, 3],
                  [3, 22, 4]]
l = 0
print("|-|-|-|  MAQUINA DE ESTADOS FINITA  |-|-|-|\n")
print("Digite 1 para entrada de um Estado")
entrada = int(input("Digite 2 para entrada de uma Transicao\n"))
if entrada == 1:
    print("\nEscolha uma dessas opcoes de Estados abaixo: \n")
    print("Digite 1 para Acordado")
    print("Digite 2 para Trabalhando")
    print("Digite 3 para Descansando")
    EstadoAtual = int(input("Digite 4 para Dormindo\n"))
    cont = 0
    while l < 6:
        c = 0
        if EstadoAtual == relacionamento[l][c] and cont == 0:
            c = 1
            print("A proxima Transicao possivel sera:")
            converte(relacionamento[l][c])
            cont = 1
        elif EstadoAtual == relacionamento[l][c] and cont == 1:
            c = 1
            print("ou as")
            converte(relacionamento[l][c])

        l += 1

elif entrada == 2:
    print("\nEscolha uma dessas opcoes de Transições abaixo: \n")
    print("Digite 8 para 8h")
    print("Digite 9 para 9h")
    print("Digite 12 para 12h")
    print("Digite 13 para 13h")
    print("Digite 18 para 18h")
    TransicaoAtual = int(input("Digite 22 para 22h\n"))
    while l < 6:
        c = 1
        if TransicaoAtual == relacionamento[l][c]:
            c = 2
            print("\nA maquina se encontra no estado:")
            converte(relacionamento[l][c])
        l += 1
