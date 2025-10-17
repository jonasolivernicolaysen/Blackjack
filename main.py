from enum import Enum
from typing import Iterable
import random


class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"


class Rank(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "T"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"


class Card():
    def __init__(self, suit: Suit,  rank: Rank,) -> None:
        self.suit = suit
        self.rank = rank
    
    @property
    def value(self) -> tuple:
        if self.rank in (Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING):
            return (10,)
        elif self.rank == Rank.ACE:
            return (1, 11)
        else:
            return (int(self.rank.value),)

    def __repr__(self) -> str:
        return f"{self.rank}{self.suit}"


class Hand():
    def __init__(self) -> None:
        self.hand = []

    def add(self, card: Card) -> None:
        self.hand.append(card)

    def current_hand_value(self) -> int:
        aces = sum(1 for card in self.hand if card.rank == Rank.ACE)
        total = sum(card.value[0] for card in self.hand if card.rank != Rank.ACE) + aces
        while aces and total + 10 <= 21:
            total += 10; aces -= 1
        return total

    def __repr__(self):
        return ", ".join([f"{card.rank.value}{card.suit.value}" for card in self.hand])
    

class Deck():
    def __init__(self) -> None:
        self.deck = [
            Card(suit, rank) for suit in Suit for rank in Rank
        ]

    @property
    def length(self):
        return len(self.deck)
        
    def shuffle(self) -> None:
        return random.shuffle(self.deck)
    
    def get(self):
        return self.deck
    
    def deal(self):
        return self.deck.pop()
    
    def __repr__(self) -> str:
        return ", ".join([f"{card.rank.value}{card.suit.value}" for card in self.deck])


class GameEngine():
    def __init__(self, deck) -> None:
        self.deck = deck
        self.player = Hand()
        self.dealer = Hand()
        self.balance = 100

    def _deal_initial(self):
        self.player.add(self.deck.deal())
        self.player.add(self.deck.deal())
        self.dealer.add(self.deck.deal())

    def start(self):
        self._deal_initial()

    def new_round(self):
        if self.deck.length < 15:
            self.deck = Deck()
            self.deck.shuffle()
        self.player = Hand()
        self.dealer = Hand()
        self._deal_initial()

    def hit_player(self):
        self.player.add(self.deck.deal())
    
    def dealer_play(self):
        while self.dealer.current_hand_value() < 17 and \
            self.dealer.current_hand_value() < self.player.current_hand_value():
            self.dealer.add(self.deck.deal())
            
    def outcome(self):
        if (self.player.current_hand_value() == self.dealer.current_hand_value()) \
        and self.player.current_hand_value() <= 21:
            return "Push"

        elif (self.player.current_hand_value() > 21) \
        or self.player.current_hand_value() < self.dealer.current_hand_value() and self.dealer.current_hand_value() <= 21:
            return "Dealer wins"
        
        elif (self.dealer.current_hand_value() > 21) \
        or self.dealer.current_hand_value() < self.player.current_hand_value() and self.player.current_hand_value() <= 21:
            return "Player wins"
        

        