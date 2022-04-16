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

# game loop
for _ in range(2):
        darCarta(maoDoDealer)
        darCarta(maoDoJogador)

while jogadorIn or dealerIn:
        print(f"Dealer had {revelarMaoDealer()} and X" )
        print(f"You have {maoDoJogador} for a total of {total(maoDoJogador)}")
        if jogadorIn:
                stayOrHit = input("1: Stay\n2: Hit\n")
        if total(maoDoDealer) > 16:
                delaerIn = False
        else:
                darCarta(maoDoDealer)
        if stayOrHit == '1':
                jogadorIn = False
        else:
                darCarta(maoDoJogador)
        if total(maoDoJogador) >= 21:
                break
        elif total(maoDoDealer) >= 21:
                break

        if total(maoDoJogador) == 21:
                print(f"\n You have {maoDoJogador} for a total of 21 and the dealer has {maoDoDealer} for a total of {(maoDoDealer)}")
                print("Blackjack! you win!")
        elif total(maoDoDealer) == 21:
                print(f"\n You have {maoDoJogador} for a total of 21 and the dealer has {maoDoDealer} for a total of {(maoDoDealer)}")
                print("Blackjack! Dealer wins!")
        elif total(maoDoJogador) > 21:
                print(f"\n You have {maoDoJogador} for a total of 21 and the dealer has {maoDoDealer} for a total of {(maoDoDealer)}")
                print("You bust! Dealer wins!")
        elif total(maoDoDealer) == 21:
                print(f"\n You have {maoDoJogador} for a total of 21 and the dealer has {maoDoDealer} for a total of {(maoDoDealer)}")
                print("Dealer Busts! You win!")
        elif 21 - total(maoDoDealer) < 21 - total(maoDoJogador):
                print(f"\n You have {maoDoJogador} for a total of 21 and the dealer has {maoDoDealer} for a total of {(maoDoDealer)}")
                print("Dealer wins!")
        elif 21 - total(maoDoDealer) > 21 - total(maoDoJogador):
                print(f"\n You have {maoDoJogador} for a total of 21 and the dealer has {maoDoDealer} for a total of {(maoDoDealer)}")
                print("You win!")
