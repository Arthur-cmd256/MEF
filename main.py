import PySimpleGUI as sg

layout = [[sg.Text("Digite 1 para entrada de um Estado")],
          [sg.Text("Digite 2 para entrada de uma Transicao")],
          [sg.InputText(key='-ENTRADA-')],
          [sg.Button("Confirmar")]]

# Crio janela
window = sg.Window("MAQUINA DE ESTADOS FINITA", layout, margins=(100, 50))

# Aqui a gente cuida dos eventos
while True:
    # aqui eu leio os eventos que talvez estejam ocorrendo
    evento, valores = window.read()
    if evento == "Confirmar" or evento == sg.WIN_CLOSED:
        break
window.close()


# Essa função converte
def converte(resultado):
    if resultado == 1:
        return "Acordado"
    elif resultado == 2:
        return "Trabalhando"
    elif resultado == 3:
        return "Descansando"
    elif resultado == 4:
        return "Dormindo"
    elif resultado == 8:
        return "8 horas"
    elif resultado == 9:
        return "9 Horas"
    elif resultado == 12:
        return "12 horas"
    elif resultado == 13:
        return "13 horas"
    elif resultado == 18:
        return "18 horas"
    elif resultado == 22:
        return "22 Horas"


relacionamento = [[4, 8, 1],
                  [1, 9, 2],
                  [2, 12, 3],
                  [3, 13, 2],
                  [2, 18, 3],
                  [3, 22, 4]]
l = 0
# print("|-|-|-|  MAQUINA DE ESTADOS FINITA  |-|-|-|\n")
# print("Digite 1 para entrada de um Estado")
# entrada = int(input("Digite 2 para entrada de uma Transicao\n"))
entrada = int(valores['-ENTRADA-'])
if entrada == 1:
    # print("\nEscolha uma dessas opcoes de Estados abaixo: \n")
    # print("Digite 1 para Acordado")
    # print("Digite 2 para Trabalhando")
    # print("Digite 3 para Descansando")
    # EstadoAtual = int(input("Digite 4 para Dormindo\n"))

    layout = [[sg.Text("Escolha uma dessas opcoes de Estados abaixo:")],
              [sg.Text("Digite 1 para Acordado")],
              [sg.Text("Digite 2 para Trabalhando")],
              [sg.Text("Digite 3 para Descansando")],
              [sg.Text("Digite 4 para Dormindo")],
              [sg.InputText(key='-ESTADO-')],
              [sg.Button("Confirmar")]]

    # Crio janela
    window = sg.Window("MAQUINA DE ESTADOS FINITA", layout, margins=(100, 50))

    # Aqui a gente cuida dos eventos
    while True:
        # aqui eu leio os eventos que talvez estejam ocorrendo
        evento, valores = window.read()
        if evento == "Confirmar" or evento == sg.WIN_CLOSED:
            break
    window.close()
    EstadoAtual = int(valores['-ESTADO-'])
    cont = 0
    while l < 6:
        c = 0
        if EstadoAtual == relacionamento[l][c] and cont == 0:
            c = 1
            # print("A proxima Transicao possivel sera:")
            # converte(relacionamento[l][c])
            sg.popup("A proxima transicao possivel sera as " + str(converte(relacionamento[l][c])))
            cont = 1
        elif EstadoAtual == relacionamento[l][c] and cont == 1:
            c = 1
            # print("ou as")
            # converte(relacionamento[l][c])
            sg.popup("Ou também as " + str(converte(relacionamento[l][c])))

        l += 1

elif entrada == 2:
    # print("\nEscolha uma dessas opcoes de Transições abaixo: \n")
    # print("Digite 8 para 8h")
    # print("Digite 9 para 9h")
    # print("Digite 12 para 12h")
    # print("Digite 13 para 13h")
    # print("Digite 18 para 18h")
    # TransicaoAtual = int(input("Digite 22 para 22h\n"))

    layout = [[sg.Text("Escolha uma dessas opcoes de Transições abaixo:")],
              [sg.Text("Digite 8 para 8h")],
              [sg.Text("Digite 9 para 9h")],
              [sg.Text("Digite 12 para 12h")],
              [sg.Text("Digite 13 para 13h")],
              [sg.Text("Digite 18 para 18h")],
              [sg.Text("Digite 22 para 22h")],
              [sg.InputText(key='-TRANSICAO-')],
              [sg.Button("Confirmar")]]

    # Crio janela
    window = sg.Window("MAQUINA DE ESTADOS FINITA", layout, margins=(100, 50))

    # Aqui a gente cuida dos eventos
    while True:
        # aqui eu leio os eventos que talvez estejam ocorrendo
        evento, valores = window.read()
        if evento == "Confirmar" or evento == sg.WIN_CLOSED:
            break
    window.close()
    TransicaoAtual = int(valores['-TRANSICAO-'])

    while l < 6:
        c = 1
        if TransicaoAtual == relacionamento[l][c]:
            c = 2
            # print("\nA maquina se encontra no estado:")
            # converte(relacionamento[l][c])
            sg.popup("A maquina se encontra no estado " + str(converte(relacionamento[l][c])))
        l += 1
