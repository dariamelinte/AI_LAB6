NUMBER_TABLE = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

INITIAL_TABLE = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def equals3(a, b, c):
    return a == b and b == c and a != 0

class Player:
    USER = 1
    COMPUTER = 2

scores = {
    Player.COMPUTER: 10,
    Player.USER: -10,
    0: 0
}
