import time
import random


def player():
    player = input("Anna nimesi: ")
    p_cards(player)


def p_cards(player):
    print("Pelataan tikkiä, tervetuloa pelaamaan:", player)
    cards = ["risti2","risti3","risti4","risti5","risti6","risti7","risti8","risti9","risti10","risti11","risti12","risti13","risti14","ruutu2","ruutu3","ruutu4","ruutu5","ruutu6","ruutu7","ruutu8","ruutu9","ruutu10","ruutu11","ruutu12","ruutu13","ruutu14","hertta2","hertta3","hertta4","hertta5","hertta6","hertta7","hertta8","hertta9","hertta10","hertta11","hertta12","hertta13","hertta14","pata2","pata3","pata4","pata5","pata6","pata7","pata8","pata9","pata10","pata11","pata12","pata13","pata14"]
    player = get_unique_numbers(cards) # arvotaan 5 korttia pelaajalle
    print("Player cards:", player)
    
    # poistetaan arvotut kortit pelipatakasta
    for i in cards:
        if i in player:
            # print("found", i)
            cards.remove(i)
    r_cards = cards # vaihdetaan uusi muuttuja
    
    c_cards(r_cards)

    

def c_cards(r_cards):
    # print("Arvotaan tietokoneen kortit")
    computer = (get_unique_numbers(r_cards))
    print("Computer cards", computer)


def get_unique_numbers(numbers):
    unique = []
    c_amount = 0 # korttien määrä
    for number in numbers:
        number = random.choice(numbers) # arvotaan kortit
        if c_amount == 5:
            break
        if number in unique:
            continue
        else:
            unique.append(number)
            c_amount += 1
    return unique

player()

"""
a = ['1','2','3']
b = ['2','5']
    
for i in a:
    if i in b:
        print("found", i)
        b.remove(i)
print(b)

"""