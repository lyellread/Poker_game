from hand_class import *
from cards_deck import *


class Player:
    def __init__(
        self, name, starting_chip_stack, player_info_filename, poker_hands_filename
    ):
        self.name = name
        self.hand = Hand()
        self.chip_stack = starting_chip_stack
        self.bet = 0
        self.legs = 0
        self.player_info_filename = player_info_filename
        self.poker_hands_filename = poker_hands_filename

        # create random key
        self.deck_multiplier = random.randint(1, 886)
        self.card_offset = random.randint(0, 46132)
        self.card_multiplier = random.randint(1, 46132)

        player_info = open(self.player_info_filename, "a")
        info_string = f"{self.name}\n"
        info_string += f"card offset = {self.card_offset}, card multiplier = {self.card_multiplier}"
        print(info_string, file=player_info)

    def auntie(self, amount):
        """
        amount = int
        Funtion to remove the auntie amount from a players chip stack
        """

        self.chip_stack -= amount

    def __str__(self):
        return f"{self.name}: chip stack is {self.chip_stack}, hand is \n{str(self.hand)}\n"

    def reveal_hand(self, card_color: bool):
        for card in self.hand.cards:
            card.type = "up"
        print(f"{self.name}\n{self.hand.display_hand(card_color)}")

    def reveal_card(self, index):
        """
        index = int (location in player hand of target card)
        Changes target card type to up
        """
        self.hand.cards[index].type = "up"

    def pass_cards(self, cards: list):
        """
        cards = list of indexes of cards to pass
        returns a list of the cards passed
        """
        # get cards to pass
        passing_cards = []
        for card_i in cards:
            passing_cards.append(self.hand.cards[card_i])
        # remove passed cards from players hand
        for card in passing_cards:
            self.hand.remove_card(card)
        return passing_cards

    def print_hand_to_file(self):
        poker_hands = open(self.poker_hands_filename, "a")
        hand_string = f"{self.name}\n"

        for card in self.hand.cards:
            hand_string += f"{card}, "
        print(hand_string, file=poker_hands)
        return None

    def coded_str_player(self, deck_code, card_color):
        return f"{self.name}: chip stack is {self.chip_stack}, hand is \n{self.hand.coded_str_hand(self, deck_code, card_color)}\n"
