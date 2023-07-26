import random

def jogo_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]

    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    print("Você vai competir contra o computador. Escolha: pedra, papel ou tesoura.")

    while True:
        # Solicita a escolha do jogador (em minúsculas para evitar problemas com a comparação posterior)
        jogador = input("Digite sua escolha (pedra/papel/tesoura) ou 'sair' para sair do jogo: ").lower()

        if jogador == 'sair':
            print("Obrigado por jogar!")
            break

        if jogador not in opcoes:
            # Verifica se a escolha do jogador é válida
            print("Opção inválida. Escolha entre pedra, papel ou tesoura.")
            continue

        # O computador faz sua escolha aleatoriamente
        computador = random.choice(opcoes)

        print(f"Você escolheu: {jogador}")
        print(f"Computador escolheu: {computador}")

        if jogador == computador:
            print("Empate!")  # Caso em que jogador e computador escolhem a mesma opção
        elif (
            (jogador == "pedra" and computador == "tesoura") or
            (jogador == "papel" and computador == "pedra") or
            (jogador == "tesoura" and computador == "papel")
        ):
            print("Parabéns! Você venceu!")  # Caso em que o jogador vence o computador
        else:
            print("O computador venceu!")  # Caso em que o computador vence o jogador

if __name__ == "__main__":
    jogo_pedra_papel_tesoura()
