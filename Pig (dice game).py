# Hur många spelare?
# Vilka namn?
# Random spelare börjar
# (Slumpa tal 1-6
# Om 1, nästa spelare
# Om 2-6, addera till roundscore, play again?
# Om ja, play again
# Om nej, vinst?
# Om ja, gameover
# Om nej, nästa spelare) loopa

import random


class Player:
    def __init__(self, name):
        self.name = name
        self.roundpoints = 0
        self.totalpoints = 0

    def __str__(self):
        return self.name


class Pig:
    def __init__(self):
        self.players = []
        self.player_number = 0
        self.current_player = 0

    def players_program(self):
        how_many_players = int(input("Hur många spelare är ni? "))
        for i in range(how_many_players):
            self.players.append(Player(self.create_player(i + 1)))
        return self.players

    def create_player(self, i):
        return Player(input(f"Vad är spelare {i}'s namn? "))

    def run(self):
        abort = False
        print("Hello och välkommen till spelet Pig")
        self.players_program()
        while not abort:
            self.player_turn()

    def player_turn(self):

        player_choice = input(f"""
        It is 's turn, r - Roll, n - Next round, q - Quit
        Choose your next move!
        """)
        if player_choice == "r":
            self.r_input()
        #elif player_choice == "n":
            #n_input()
        #elif player_choice == "q":
            #q_input()

    def choose_random_player(self):
        self.current_player = random.randint(0, )

    def roll_dice(self):

        return random.randint(1, 6)

    def r_input(self):
        current_dice_result = self.roll_dice()
        if current_dice_result == 1:
            return
        else:
            self.current_player.roundpoints += current_dice_result








def pick_random_number(upper_limit):
    return random.randint(0, upper_limit)





    #random_player_start = pick_random_player(len(all_players))
    #for i in range(1000):
    #
    #    if player_choice == "n":
    #        all_players[i % len(all_players)].totalpoints = all_players[i % len(all_players)].roundpoints
    #    elif player_choice == "q":
    #        break

    #       current_dice_result = roll_dice()
    #    if current_dice_result == 1:
    #        pass
    #    else:
    #        all_players[0].roundpoints += current_dice_result
    #        print(all_players[0].roundpoints)




if __name__ == "__main__":
    pig = Pig()
    pig.run()


