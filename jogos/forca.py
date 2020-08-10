def jogar():
    print("\n******************************************************************")
    print("*            Bem vindo ao jogo de ---FORCA--- !!!         *")
    print("******************************************************************")

    palavra_secreta = "guitarra"
    enforcado = False
    acertou = False

    # Roda o jogo enquanto o jogador não acertar a palavra, e não tiver esgotado todas as tentativas disponíves.
    while not enforcado and not acertou:
        print("Jogando...")

    print("\n******************************************************************")
    print("*                        Fim do jogo !!!                         *")
    print("******************************************************************")

if __name__ == "__main__":
    jogar()