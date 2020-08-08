# Importação do jogo de Adivinhações.
import adivinhacao

# Exibe os jogos disponpiveis ao jogador, e solicita que um deles seja escolhido;
# Caso seja informada uma opção inválida, solicita novamente ao jogador (enquanto não informar uma opção válida).
jogo_selecionado = -1
while jogo_selecionado == -1:
    jogo_selecionado = int(input(
        "\nEscolha um jogo: \n1 - Adivinhações \n0 - SAIR \n-> Jogo selecionado: "))

    if jogo_selecionado == 0:
        print("\nAté a próxima!!!")
    elif jogo_selecionado == 1:
        adivinhacao.jogar()
    else:
        jogo_selecionado = -1
        nivel = input(
            "\nOpção inválida!!!\nEscolha um jogo: \n1 - Adivinhações \n0 - SAIR \n-> Jogo selecionado: ")
