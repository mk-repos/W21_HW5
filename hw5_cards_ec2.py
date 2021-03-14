#########################################
##### Name:     Moeki Kurita        #####
##### Uniqname: mkurita             #####
#########################################

import random
import unittest

VERSION = 0.01

class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order 
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades
    
    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds","Clubs","Hearts","Spades"]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}


    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)

    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"


class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self):

        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order

    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters  
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i)

    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list

    def sort_cards(self):
        '''returns the Deck to its original order
        
        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck
        
        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters  
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self, num_hands: int, num_cards: int):
        """Deal cards to given number of hands
        Distribute given number of cards to each hand

        Parameters
        ----------
        num_hands : int
            number of hands to be created
        num_cards : int
            number of cards to be given to each hand
            if given -1, distribute all cards of the deck

        Returns
        -------
        list
            a list of resulting Hands
            empty if the requested parameters are too large
        """
        hands = []
        # if too many cards are requested
        if num_hands*num_cards > len(self.cards):
            print("Not enough cards in the deck. Returning empty list.")
        # if the deck has enough number of cards to deal
        elif num_cards != -1:
            for hand in range(num_hands):
                hands.append(Hand(self.deal_hand(num_cards)))
        # if -1 was given
        elif num_cards == -1:
            # in case we can create hands with even number of cards
            if len(self.cards) % num_hands == 0:
                hand_size = int(len(self.cards)/num_hands)
                for hand in range(num_hands):
                    hands.append(Hand(self.deal_hand(hand_size)))
            # in case number of cards cannot be even
            else:
                hand_size = len(self.cards)//num_hands
                for hand in range(num_hands):
                    hands.append(Hand(self.deal_hand(hand_size)))
                remainder = len(self.cards) % num_hands
                for i in range(remainder):
                    hands[i].cards.append(self.cards.pop())
        return hands


class Hand:
    '''a hand for playing card
    
    Class Attributes
    ---------------
    None
    
    Instance Attributes
    ------------------
    init_card: list
        a list of cards
    '''

    def __init__(self, init_cards):
        self.cards = init_cards

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand

        Parameters
        ----------
        card: instance
            a card to add

        Returns
        -------
        None
        '''
        card_strs = []
        for c in self.cards:
            card_strs.append(c.__str__())
        if card.__str__() not in card_strs:
            self.cards.append(card)

    def remove_card(self, card):
        '''remove a card from the hand
        
        Parameters
        ----------
        card: instance
            a card to remove
        
        Returns
        -------
        the card, or None if the card was not in the Hand
        '''
        card_strs = []
        for c in self.cards:
            card_strs.append(c.__str__())
        if str(card) in card_strs:
            position = card_strs.index(str(card))
            return self.cards.pop(position)
        else:
            return None

    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card
        
        Parameters
        ----------
        deck: instance
            a deck from which to draw

        Returns
        -------
        None
        '''
        draw = deck.deal_card()
        self.add_card(draw)

    def remove_pairs(self):
        """Looks for pairs of cards and removes them
        Iterately check if the hand has duplicates
        Delete pairs (leave one of three of a kind)
        """
        # create list of ranks
        cards_ranks = []
        for c in self.cards:
            cards_ranks.append(c.rank)
        # count duplicates of each rank
        count_dict = {rank: cards_ranks.count(rank) for rank in cards_ranks}
        # delete duplicates
        for k, v in count_dict.items():
            # get positions for the rank
            indices = [index for index, value in enumerate(cards_ranks)
                       if value == k]
            # three of a kind
            if v == 3:
                # delete only two of them
                for i in reversed(indices[-2:]):
                    self.cards.pop(i)
            # pair or four of a kind
            if v == 2 or v == 4:
                # delete all occurences
                for i in reversed(indices):
                    self.cards.pop(i)


def print_hand(hand):
    '''prints a hand in a compact form
    
    Parameters  
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)