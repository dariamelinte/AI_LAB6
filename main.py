import random

from models.game import Game
from models.player import Player

def main():
    print("Hello. You are going to play the game 'Number Scrabble'.")
    
    game = Game()

    while not game.is_over():
        print(f"Turn: {game.turn}")
        print(f"Available numbers: {game.available_numbers}")

        is_valid = False

        if game.turn == Player.USER:
            user_input = input("Enter your next number: ")
            user_number = int(user_input)

            is_valid = game.mark_chosen_number(user_number)

        if game.turn == Player.CALCULATOR:
            calc_number = random.randint(1, 9)

            is_valid = game.mark_chosen_number(calc_number)

        if is_valid:
            game.turn = 1 - game.turn


    game.win_announcement()
        









if __name__ == "__main__":
    main()
