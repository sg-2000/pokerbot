import random


BACK = "🂠 "
CARDS = [
    #id suit glyph value   name
    (1,  0,  "🂡 ",   14,   "Ace of Spades"),
    (2,  0,  "🂢 ",    2,   "Two of Spades"),
    (3,  0,  "🂣 ",    3,   "Three of Spades"),
    (4,  0,  "🂤 ",    4,   "Four of Spades"),
    (5,  0,  "🂥 ",    5,   "Five of Spades"),
    (6,  0,  "🂦 ",    6,   "Six of Spades"),
    (7,  0,  "🂧 ",    7,   "Seven of Spades"),
    (8,  0,  "🂨 ",    8,   "Eight of Spades"),
    (9,  0,  "🂩 ",    9,   "Nine of Spades"),
    (10, 0,  "🂪 ",   10,   "Ten of Spades"),
    (11, 0,  "🂫 ",   11,   "Jack of Spades"),
    (12, 0,  "🂭 ",   12,   "Queen of Spades"),
    (13, 0,  "🂮 ",   13,   "King of Spades"),
    (14, 1,  "🂱 ",   14,   "Ace of Hearts"),
    (15, 1,  "🂲 ",    2,   "Two of Hearts"),
    (16, 1,  "🂳 ",    3,   "Three of Hearts"),
    (17, 1,  "🂴 ",    4,   "Four of Hearts"),
    (18, 1,  "🂵 ",    5,   "Five of Hearts"),
    (19, 1,  "🂶 ",    6,   "Six of Hearts"),
    (20, 1,  "🂷 ",    7,   "Seven of Hearts"),
    (21, 1,  "🂸 ",    8,   "Eight of Hearts"),
    (22, 1,  "🂹 ",    9,   "Nine of Hearts"),
    (23, 1,  "🂺 ",   10,   "Ten of Hearts"),
    (24, 1,  "🂻 ",   11,   "Jack of Hearts"),
    (25, 1,  "🂽 ",   12,   "Queen of Hearts"),
    (26, 1,  "🂾 ",   13,   "King of Hearts"),
    (27, 2,  "🃁 ",   14,   "Ace of Diamonds"),
    (28, 2,  "🃂 ",    2,   "Two of Diamonds"),
    (29, 2,  "🃃 ",    3,   "Three of Diamonds"),
    (30, 2,  "🃄 ",    4,   "Four of Diamonds"),
    (31, 2,  "🃅 ",    5,   "Five of Diamonds"),
    (32, 2,  "🃆 ",    6,   "Six of Diamonds"),
    (33, 2,  "🃇 ",    7,   "Seven of Diamonds"),
    (34, 2,  "🃈 ",    8,   "Eight of Diamonds"),
    (35, 2,  "🃉 ",    9,   "Nine of Diamonds"),
    (36, 2,  "🃊 ",   10,   "Ten of Diamonds"),
    (37, 2,  "🃋 ",   11,   "Jack of Diamonds"), 
    (38, 2,  "🃍 ",   12,   "Queen of Diamonds"),
    (39, 2,  "🃎 ",   13,   "King of Diamonds"),
    (40, 3,  "🃑 ",   14,   "Ace of Clubs"),
    (41, 3,  "🃒 ",    2,   "Two of Clubs"),
    (42, 3,  "🃓 ",    3,   "Three of Clubs"),
    (43, 3,  "🃔 ",    4,   "Four of Clubs"),
    (44, 3,  "🃕 ",    5,   "Five of Clubs"),
    (45, 3,  "🃖 ",    6,   "Six of Clubs"),
    (46, 3,  "🃗 ",    7,   "Seven of Clubs"),
    (47, 3,  "🃘 ",    8,   "Eight of Clubs"),
    (48, 3,  "🃙 ",    9,   "Nine of Clubs"),
    (49, 3,  "🃚 ",   10,   "Ten of Clubs"),
    (50, 3,  "🃛 ",   11,   "Jack of Clubs"),
    (51, 3,  "🃝 ",   12,   "Queen of Clubs"),
    (52, 3,  "🃞 ",   13,   "King of Clubs")
]

class Card():
    def __init__(self, card):
        self.id = card[0]
        self.suit = card[1]
        self.glyph = card[2]
        self.value = card[3]
        self.name  = card[4]
        
class Deck():
    def __init__(self):
        self.cards = []
        for card in CARDS:
            self.cards.append(Card(card))
        random.shuffle(self.cards)

    def next(self):
        card = self.cards.pop(0)
        return card
