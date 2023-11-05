class Game:
    def __init__(self):
        self._players = list()
        self._turn = 0
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
