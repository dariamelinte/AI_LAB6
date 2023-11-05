import random

class Game:
    def __init__(self):
        self._players = [[], []]
        self._turn = random.randint(0, 1) # generate random initial turn
        self._available_numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players
    
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


    def is_over(self):
        return len(self.available_numbers) == 0
    
    def is_number_valid(self, number):
        return number in self.available_numbers

    def mark_chosen_number(self, number):
        if not self.is_number_valid(number):
            return False
        
        self.players[self.turn].append(number)
        self.available_numbers.discard(number)

        return True

    def win_announcement(self):
        print(f"USER: {self.players[0]}")
        print(f"CALCULATOR: {self.players[1]}")



