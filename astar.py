__author__ = 'helenetangen'



class Board:


    def makeBoard(self, height, width):
        board = [[0 for x in range(height)] for x in range(width)]
        return board


def main():
    b = Board()
    b.board = b.makeBoard(5, 5)
    for i in range(5):
        b.board[i][i] = 1
        print b.board[i][i]


if __name__ == '__main__':
    main()
