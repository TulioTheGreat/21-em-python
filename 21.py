import random
jogadorIn = True
dealerIn = True
# cartas
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
maoDoJogador = []
maoDoDealer = []
# dar as cartas
def darCarta(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calcular o total de cada mão
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11

    return total
                         
# vencedor
def revelarMaoDealer():
    if len(maoDoDealer) == 2:
        return maoDoDealer[0]
    elif len(maoDoDealer) > 2:
        return maoDoDealer[0], maoDoDealer[1]

# Placar final do jogo
def avisarPlacar():
    print(f"\nVocê terminou com: {maoDoJogador}, totalizando {total(maoDoJogador)} pontos e o Ding Liren terminou com: {maoDoDealer}, totalizando {total(maoDoDealer)} pontos")

# game loop
for _ in range(2):
    darCarta(maoDoDealer)
    darCarta(maoDoJogador)

while jogadorIn and dealerIn:
    # print(f"O Ding Liren tirou: {revelarMaoDealer()} e X" )
    print(f"Você tem {maoDoJogador} e {total(maoDoJogador)} pontos")

    if jogadorIn:
        stayOrHit = input("1: Pedir outra carta\n2: Descer cartas\n")
    if total(maoDoDealer) > 16:
        dealaerIn = False
    else:
        darCarta(maoDoDealer)
    if stayOrHit == '2':
        jogadorIn = False
    else:
        darCarta(maoDoJogador)
    if total(maoDoJogador) >= 21:
        jogadorIn = False
    elif total(maoDoDealer) >= 21:
        dealerIn = False

    if total(maoDoJogador) == 21:
        avisarPlacar()
        print("Vinte e um! Você ganhou!")
    elif total(maoDoDealer) == 21:
        avisarPlacar()
        print("Vinte e um! O Ding Liren ganha!")
    elif total(maoDoJogador) > 21:
        avisarPlacar()
        print("Você estourou! O Ding Liren ganha!")
    elif total(maoDoDealer) == 21:
        avisarPlacar()
        print("O Ding Liren estourou! Você ganhou!")
    elif 21 - total(maoDoDealer) < 21 - total(maoDoJogador):
        avisarPlacar()
        print("Ding Liren ganha!")
    elif 21 - total(maoDoDealer) > 21 - total(maoDoJogador):
        avisarPlacar()
        print("Você venceu!")
