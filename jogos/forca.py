def jogar():
    print("\n******************************************************************")
    print("*            Bem vindo ao jogo de ---FORCA--- !!!         *")
    print("******************************************************************")

    palavra_secreta = "guitarra"
    enforcado = False
    acertou = False

    # Roda o jogo enquanto o jogador não acertar a palavra, e não tiver esgotado todas as tentativas disponíves.
    while not enforcado and not acertou:

        chute = input("-> Digite uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if letra.upper() == chute.upper():
                print(f"Encontrei a letra {letra} na posição {index}")

            index = index + 1

    print("\n******************************************************************")
    print("*                        Fim do jogo !!!                         *")
    print("******************************************************************")

if __name__ == "__main__":
    jogar()