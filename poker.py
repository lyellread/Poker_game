import random
import os
from game_play import *
from player_class import *
from hand_class import *
from cards_deck import *


def main():

    # initialize variables
    dealer_i = 0

    games = [
        "Baseball",
        "Queens",
        "Whores",
        "Nicks",
        "Texas",
        "Omaha",
        "test",
        "0/54",
        "7_card_screw",
        "Elevator",
        "1_card_screw",
        "D_and_G",
        "Kings",
        "7/27",
    ]

    player_info_filename = "player_info.txt"
    poker_hands_filename = "player_poker_hands.txt"

    starting_chip_stack = int(input("Enter starting chip stack amount: "))
    ante = int(input("Enter ante amount for games: "))

    # determine card color selection
    card_color = "y" == input("Do you want to use colored cards? y/n: ")

    # set up players
    players = []
    player_info = open(player_info_filename, "w")
    player_info.close()

    # fill player array
    while True:

        player_name = input("Enter player name (press Enter to move on): ")
        if player_name == "" and len(players) > 0:
            break
        elif player_name == "" and len(players) == 0:
            print("Error: At least one player is needed!")
        else:
            players.append(
                Player(
                    player_name,
                    starting_chip_stack,
                    player_info_filename,
                    poker_hands_filename,
                )
            )

    while True:
        print(f"\nNew game,", str(players[dealer_i].name), "is dealer")

        # reset all hands
        for player in players:
            player.hand.reset()
            print(player)

        gametype = input(
            "What do you want to do?\n"
            " + Administrative Actions:\n"
            "  - game over\n"
            "  - remove player\n"
            "  - add player\n"
            " + Game Types:\n  - " + "\n  - ".join(games) + "\n\nChoice: "
        )

        if gametype == "game over":

            # remove the files that were created at game over time
            if player_info_filename in os.listdir("."):
                os.remove(player_info_filename)

            if poker_hands_filename in os.listdir("."):
                os.remove(poker_hands_filename)

            break

        elif gametype == "remove player":
            name = input("What is the name of the player to remove? ")
            if player in players:
                players.remove(player)

        elif gametype == "add player":
            name = input("Enter plyer name: ")
            players.append(Player(name))

        elif gametype not in games:
            print("\nPlease enter a valid game\n\n\n")
            pass

        else:
            game = Game(
                gametype, players, dealer_i, ante, card_color, poker_hands_filename
            )
            game.play()

            # increment dealer, loop if needed
            dealer_i = (dealer_i + 1) % (len(players))

        # reset players hands and bet amount
        for player in players:
            player.hand.reset()
            player.bet = 0


if __name__ == "__main__":
    main()
