import random
from game_play import *
from player_class import *
from hand_class import *
from cards_deck import *



def main():

    #initialize variables
    dealer_i =  0

    games = ["Baseball", 
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
            "7/27"]

    starting_chip_stack = int(input("Enter starting chip stack amount: "))
    auntie = int(input("Enter auntie amount for games: "))

    #determine card color selection
    card_color = 'y' == input("Do you want to use colored cards? y/n: ")

    #set up players
    players = []
    player_info = open('player_info.txt', 'w')
    player_info.close()
    
    #fill player array
    while(True):

        player_name = input("Enter player name (type 'done' to move on): ")
        if player_name == "done":
            break
        players.append(Player(player_name, starting_chip_stack))

    while(True):
        print(f"\nNew game, {players[dealer_i].name} is dealer")

        #reset all hands
        for player in players:
            player.hand.reset()
            print(player)

        print("What game should we play? Type 'game over' to end, 'remove player' to remove a player, 'add player' to add a player.")
        gametype = input("Game Options: " + ', '.join(games) + ": ")

        if gametype == "game over":
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
            game = Game(gametype, players, dealer_i, auntie, card_color)
            game.play()

            # increment dealer, loop if needed
            dealer_i = (dealer_i + 1) % (len(players))

        #reset players hands and bet amount
        for player in players:
            player.hand.reset()
            player.bet = 0


if __name__ == "__main__":
    main()
