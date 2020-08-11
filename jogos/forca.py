def jogar():
    print("\n******************************************************************")
    print("*            Bem vindo ao jogo de ---FORCA--- !!!         *")
    print("******************************************************************")

    palavra_secreta = "guitarra"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_"]
    enforcado = False
    acertou = False

    print(f"\n{letras_acertadas}")

    # Roda o jogo enquanto o jogador não acertar a palavra, e não tiver esgotado todas as tentativas disponíves.
    while not enforcado and not acertou:

        chute = input("-> Digite uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if letra.upper() == chute.upper():
                letras_acertadas[index] = letra

            index = index + 1

        print(f"\n{letras_acertadas}")

        acertou = letras_acertadas.count('_') == 0
        if not acertou:
            print(f"Ainda falta acertar {letras_acertadas.count('_')} letras")

    print("\n******************************************************************")
    print("*                        Fim do jogo !!!                         *")
    print("******************************************************************")

if __name__ == "__main__":
    jogar()