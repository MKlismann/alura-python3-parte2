# Importação do módulo que gera números aleatórios.
import random

def jogar():
    print("\n******************************************************************")
    print("*            Bem vindo ao jogo de ---ADIVINHAÇÕES--- !!!         *")
    print("******************************************************************")

    # Geração do número aleatório; a função random() gera números entre 1 e 101-1.
    numero_secreto = round(random.randrange(1, 101))

    # Pontuação inicial do jogador.
    pontos = 1000

    # Define a quantidade máxima de tentativas/palpites no jogo, de acordo com o nível escolhido pelo jogador.
    total_de_tentativas = 0
    nivel = int(input(
        "\nEscolha o nível de dificuldade do jogo \n1 - Fácil \n2 - Médio \n3 - Difícil \n-> Nível selecionado: "))
    while total_de_tentativas == 0:
        if nivel == 1:
            total_de_tentativas = 20
        elif nivel == 2:
            total_de_tentativas = 10
        elif nivel == 3:
            total_de_tentativas = 5
        else:
            nivel = input(
                "\nOpção inválida!!!\nEscolha o nível de dificuldade do jogo \n1 - Fácil \n2 - Médio \n3 - Difícil \n-> Nível selecionado: ")

    print(f"\nSua pontuação inicial é de {pontos} pontos.")

    for rodada in range(1, total_de_tentativas + 1):
        print(f"\nTentativa {rodada} de {total_de_tentativas}.")
        chute = int(input("-> Digite um número (palpite) entre 1 e 100: "))
        print(f"\nVocê digitou: {chute}.")

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!!!")
            continue

        palpite_correto = chute == numero_secreto
        palpite_maior = chute > numero_secreto
        palpite_menor = chute < numero_secreto

        if palpite_correto:
            print("Parabéns, você acertou! :)")
            print(f"Sua pontuação final foi de {pontos} pontos.")
            break
        else:
            if palpite_maior:
                print("Que pena, você errou! :(  O seu palpite foi maior do que o número secreto.")
            elif palpite_menor:
                print("Que pena, você errou! :(  O seu palpite foi menor do que o número secreto.")

            # Cada palpite errado causa uma perda de pontos de acordo com a seguinte regra:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print(f"Sua pontuação sofreu uma penalidade de -{pontos_perdidos} pontos.")
            print(f"Sua pontuação atual é de {pontos} pontos.")

        # Se o jogador errar todas as tentativas/palpites, informa qual era o número secreto;
        if rodada == total_de_tentativas and not palpite_correto:
            print(f"\nO número secreto era: {numero_secreto}")

        rodada = rodada + 1

    print("\n******************************************************************")
    print("*                        Fim do jogo !!!                         *")
    print("******************************************************************")

if __name__ == "__main__":
    jogar()