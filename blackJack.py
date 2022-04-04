import random
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing=True

class card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank +" of "+  self.suit

class Deck():
    def __init__(self):
        self.deck=[]

        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))

    def __str__(self):
        deck_comp= ' '
        for card in self.deck:
            deck_comp+='\n'+card.__str__() #for printing the deck of cards
        return "The deck has: "+deck_comp


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
        return single_card


class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]

    def adjust_for_aces(self):
        while self.value > 21 and self.aces > 0:
            self.value-=10
            self.aces-=1

class chips():

    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:

        try:
            chips.bet=int(input("How many chips would you ike to bet?"))

        except:
            print("sorry please provide integer")

        else:
            if chips.bet>chips.total:
                print('sorry insufficient chips to bet..you have {}'.format(chips.total))
            else:
                break

def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x=input('hit or stand? enter h or s ')

        if x[0].lower() =='h':
            hit(deck,hand)

        elif x[0].lower() =='s':
            print("player stands Dealer's turn")
            playing=False

        else:
            print("sorry, I did not understand that, please enter h or s only!")
            continue
        break

def show_some(player,dealer):
    print("\n Dealer's hand: ")
    print("first card hidden!")
    print(dealer.cards[1])

    print("\n player's hand: ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("\n player's hand: ")
    for card in player.cards:
        print(card)
    print(f"value of player's hand is:{player.value}" )

    print("\n dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"value of dealer's hand is:{dealer.value}")

def player_busts(player,dealer,chips):
    print('BUST PLAYER!')
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("player WINS!")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print('BUST DEALER!')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
def push(player,dealer):
    print("dealer and player tie! push!")

while True:

    print("WELCOME TO BLACKJACK")
    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips=chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value<=21:

        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)

        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(dealer_hand,player_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value == player_hand.value:
            push(player_hand,dealer_hand)

    print('\n player total chips are: {}'.format(player_chips.total))

    new_game=input("would you like to play again ? y/n")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print('thank you for playing')
        break









