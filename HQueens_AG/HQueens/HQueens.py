import numpy as np


class HQueens:
    def __init__(self, board=None):
        if board is None:
            self.board = np.random.randint(1, 9, size=8)

        else:
            self.board = board

    def get_attack(self, invert=False):

        nonatt = 0

        for i in range(7):
            cont = 1
            for j in range(i + 1, 8):
                if (self.board[j] != self.board[i]) and \
                        (self.board[j] != self.board[i] - cont) and \
                        (self.board[j] != self.board[i] + cont):
                    nonatt += 1

                cont += 1

        if invert:
            return 28 - nonatt

        return nonatt

    def print_board(self):
        '''
        Prints the board state.
        '''
        position = self.board - np.ones(8, dtype=int)

        size = position.size
        cheesboard = np.zeros([size, size], dtype=int)
        for i in range(size):
            cheesboard[i, position[i]] = 1

        cheesboard = np.flip(cheesboard.transpose(), 0)
        chees = []

        for i in range(cheesboard.shape[0]):
            line = []
            for j in range(cheesboard.shape[1]):
                line.append('W') if cheesboard[i, j] == 1 else line.append(' ')
            chees.append(line)

        for i in range(cheesboard.shape[0]):
            print('+---+---+---+---+---+---+---+---+')
            print(
                f'| {chees[i][0]} | {chees[i][1]} | {chees[i][2]} | {chees[i][3]} | {chees[i][4]} | {chees[i][5]} | {chees[i][6]} | {chees[i][7]} |')
        print('+---+---+---+---+---+---+---+---+')
