import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

cards = {
    1: "Ace",
    11: "Jack",
    12: "Queen",
    13: "King"
}

#takes suit and number and formats them, ex. "Ace of Spades"
def card_name(suit, cardNum):
    num = cards.get(cardNum, cardNum) # second cardNum sets default if not found in dict
    return str(num) + " of " + suit

'''
# TODO make this random
for i in range(0, 4):
    for j in range(1,13 + 1):
        print(card_name(suits[i], j))
'''

randCardNum = random.randint(1, 13 + 1)
randCardSuit = random.randint(0,3)

print(card_name(suits[randCardSuit], randCardNum))