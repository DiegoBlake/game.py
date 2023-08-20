from random import choice

comp_vitorias = 0
jogador_vitorias = 0

def opcao_jogador():
    esc_jogador = input("Escolha pedra, papel ou tesoura: ")
    if esc_jogador in ["Pedra", "PEDRA", "pedra"]:
        return "pedra"
    elif esc_jogador in ["Papel", "PAPEL", "papel"]:
        return "papel"
    elif esc_jogador in ["Tesoura", "TESOURA", "tesoura"]:
        return "tesoura"
    else:
        print("Opção inválida. Tente novamente.")
        return opcao_jogador()

def opcao_computador():
    esc_computador = choice(["pedra", "papel", "tesoura"])
    return esc_computador

while True:
    print("_____")

    esc_computador = opcao_computador()
    esc_jogador = opcao_jogador()

    print("_______")

    if (esc_jogador == "papel" and esc_computador == "pedra") or \
       (esc_jogador == "pedra" and esc_computador == "tesoura") or \
       (esc_jogador == "tesoura" and esc_computador == "papel"):
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu {esc_computador}. Resultado: você ganhou!")
        jogador_vitorias += 1

    elif esc_jogador == esc_computador:
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu {esc_computador}. Resultado: empate.")

    else:
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu {esc_computador}. Resultado: a máquina ganhou.")
        comp_vitorias += 1

    print("_______")

    print(f"Vitórias do jogador: {jogador_vitorias}")
    print(f"Vitórias da máquina: {comp_vitorias}")

    print("_______")

    esc_jogador = input("Você quer jogar novamente? (s/n)").lower()
    if esc_jogador in ["s", "sim"]:
        pass
    elif esc_jogador in ["n", "nao"]:
        break
    else:
        break
