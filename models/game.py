import random
import copy

from models.player import Player

class Game:
    def __init__(self):
        self._players = [[], []]
        self._turn = random.randint(0, 1) # generate random initial turn
        self._available_numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self._winner = -1

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players
        

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, winner):
        self._winner = winner
    
    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, turn):
        self._turn = turn
        

    @property
    def available_numbers(self):
        return self._available_numbers

    @available_numbers.setter
    def available_numbers(self, available_numbers):
        self._available_numbers = available_numbers

    def subset_sum_greedy(self, index, target_sum):
        values = copy.deepcopy(self.players[index])
        values.sort(reverse=True)

        for value in values:
            if value == target_sum:
                return True
            elif value < target_sum:
                target_sum -= value

        return target_sum == 0

    def is_over(self):
        is_user_winner = self.subset_sum_greedy(Player.USER, 15)
        is_computer_winner = self.subset_sum_greedy(Player.COMPUTER, 15)

        if is_user_winner:
            self.winner = Player.USER
        
        if is_computer_winner:
            self.winner = Player.COMPUTER

        return len(self.available_numbers) == 0 or is_user_winner or is_computer_winner
    
    def is_number_valid(self, number):
        return number in self.available_numbers

    def mark_chosen_number(self, number):
        if not self.is_number_valid(number):
            return False
        
        self.players[self.turn].append(number)
        self.available_numbers.discard(number)

        return True

    def win_announcement(self):
        print(f"Your moves: {self.players[Player.USER]}")
        print(f"Computer's moves: {self.players[Player.COMPUTER]}")

        if self.winner == Player.USER:
            print("Congratulations! You won :)")
            return

        if self.winner == Player.COMPUTER:
            print("Oopsie. The computer won :(")
            return
        
        print("Nobody won. It's a draw")

        



