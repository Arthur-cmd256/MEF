import PySimpleGUI as sg


# Essa função converte um número para retornar uma string
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

#Os dados da maquina de estados são inseridos em uma matriz
relacionamento = [["Dormindo", "8 Horas", "Acordado"],
                  ["Acordado", "9 Horas", "Trabalhando"],
                  ["Trabalhando", "12 Horas", "Descansando"],
                  ["Descansando", "13 Horas", "Trabalhando"],
                  ["Trabalhando", "18 Horas", "Descansando"],
                  ["Descansando", "22 Horas", "Dormindo"]]
entrada = 99
# Ess laço faz voltar ao menu pricipal
while entrada != 0:
    l = 0
    # print("|-|-|-|  MAQUINA DE ESTADOS FINITA  |-|-|-|\n")
    # print("Digite 1 para entrada de um Estado")
    # entrada = int(input("Digite 2 para entrada de uma Transicao\n"))
    #Configuração da primeira interface
    sg.theme('DarkAmber')

    layout = [[sg.Text("Escolha uma das opções abaixo em que você pretende inserir:")],
              [sg.Text("")],
              [sg.Button("Estado", size=(15,1)), sg.Button("Transição", size=(15,1))],
              [sg.Button("Sair", size=(15,1))]]

    # Crio janela
    window = sg.Window("MÁQUINA DE ESTADOS FINITA 2.0", layout, element_justification = 'center', font = (20), margins = (100, 50))

    # Aqui a gente cuida dos eventos
    while True:
        # aqui eu leio os eventos que talvez estejam ocorrendo
        evento, valores = window.read()
        if evento == "Estado" or evento == "Transição" or evento == "Sair" or evento == sg.WIN_CLOSED:
            break
    window.close()

    #entrada = int(valores['-ENTRADA-'])

    #Saida do laço
    if evento == "Sair":
        break
    # Condição para Estado
    if evento == "Estado":
        # print("\nEscolha uma dessas opcoes de Estados abaixo: \n")
        # print("Digite 1 para Acordado")
        # print("Digite 2 para Trabalhando")
        # print("Digite 3 para Descansando")
        # EstadoAtual = int(input("Digite 4 para Dormindo\n"))

        #Configuração da segunda interface
        layout = [[sg.Text("Escolha uma dessas opções de Estados abaixo:")],
                  [sg.Text("")],
                  [sg.Button("Acordado", size=(15,1)), sg.Button("Trabalhando", size=(15,1))],
                  [sg.Button("Descansando", size=(15,1)), sg.Button("Dormindo", size=(15,1))]]

        # Crio janela
        window = sg.Window("MÁQUINA DE ESTADOS FINITA 2.0", layout, element_justification='center', font=(20), margins=(100, 50))

        # Aqui a gente cuida dos eventos
        while True:
            # aqui eu leio os eventos que talvez estejam ocorrendo
            evento, valores = window.read()
            if evento == "Acordado" or evento == "Trabalhando" or evento == "Descansando" or evento == "Dormindo" or evento == sg.WIN_CLOSED:
                break
        window.close()

        EstadoAtual = evento
        cont = 0
        # Essa laço procura dentro da matriz o resultado desejado com o auxilio de um if
        while l < 6:
            c = 0
            if EstadoAtual == relacionamento[l][c] and cont == 0:
                c = 1
                # print("A proxima Transicao possivel sera:")
                # converte(relacionamento[l][c])
                #sg.popup("A proxima transicção possivel sera as " + str(converte(relacionamento[l][c])), font=(16))
                #imprimi o resultado das pesquisas
                sg.popup("A proxima transição possível será as " + str(relacionamento[l][c]), font=(16))
                cont = 1

            #Esse segunda condição só é ativa quando tem mais de um resultado
            elif EstadoAtual == relacionamento[l][c] and cont == 1:
                c = 1
                # print("ou as")
                # converte(relacionamento[l][c])
                #sg.popup("Ou também as " + str(converte(relacionamento[l][c])), font=(16))
                sg.popup("Ou também as " + str(relacionamento[l][c]), font=(16))

            l += 1
    # Condição para Transição
    elif evento == "Transição":
        # print("\nEscolha uma dessas opcoes de Transições abaixo: \n")
        # print("Digite 8 para 8h")
        # print("Digite 9 para 9h")
        # print("Digite 12 para 12h")
        # print("Digite 13 para 13h")
        # print("Digite 18 para 18h")
        # TransicaoAtual = int(input("Digite 22 para 22h\n"))
        #Configuração da terceira iterface
        layout = [[sg.Text("Escolha uma dessas opções de Transições abaixo:")],
                  [sg.Text("")],
                  [sg.Button("8 Horas", size=(15,1)), sg.Button("9 Horas", size=(15,1)), sg.Button("12 Horas", size=(15,1))],
                  [sg.Button("13 Horas", size=(15,1)), sg.Button("18 Horas", size=(15,1)), sg.Button("22 Horas", size=(15,1))]]

        # Crio janela
        window = sg.Window("MÁQUINA DE ESTADOS FINITA 2.0", layout, element_justification='center', font=(20), margins=(100, 50))

        # Aqui a gente cuida dos eventos
        while True:
            # aqui eu leio os eventos que talvez estejam ocorrendo
            evento, valores = window.read()
            if evento == "8 Horas" or evento == "9 Horas" or evento == "12 Horas" or evento == "13 Horas" or evento == "18 Horas" or evento == "22 Horas" or evento == sg.WIN_CLOSED:
                break
        window.close()
        TransicaoAtual = evento
        # Essa laço procura dentro da matriz o resultado desejado com o auxilio de um if
        while l < 6:
            c = 1
            if TransicaoAtual == relacionamento[l][c]:
                c = 2
                # print("\nA maquina se encontra no estado:")
                # converte(relacionamento[l][c])
                #sg.popup("A maquina se encontra no estado " + str(converte(relacionamento[l][c])))
                # imprimi o resultado das pesquisas
                sg.popup("A máquina se encontra no estado " + str(relacionamento[l][c]), font=(16))
            l += 1
