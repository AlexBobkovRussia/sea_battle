import sys
sys.path.append('.')
from random import randint
from place_battle_ships_on_the_field.place_second_place_ship import matrix
# from field_of_game.create_sea_battle_field import matrix


def wrapper(matrix, row, column):
    matrix[row - 1][column] = 0
    matrix[row + 1][column] = 0
    matrix[row][column + 1] = 0
    matrix[row][column - 1] = 0
    matrix[row - 1][column - 1] = 0
    matrix[row - 1][column + 1] = 0
    matrix[row + 1][column - 1] = 0
    matrix[row + 1][column + 1] = 0


for i in range(1, 5):
    row = randint(1, 11)
    column = randint(1, 11)
    while matrix[row][column] != '':
        row = randint(1, 11)
        column = randint(1, 11)
    matrix[row][column] = i
    wrapper(matrix, row, column)


if __name__ == '__main__':
    print(*matrix, sep="\n")

