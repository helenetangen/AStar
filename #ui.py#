__author__ = 'helenetangen'


import time
import Tkinter as tk
import threading


class UI(tk.Frame):

    def __init__(self, parent, height=5, width=5):
        tk.Frame.__init__(self, parent, background="white")
        self.parent = parent

        height = height
        width  = width

        #Make a stupid board
        board = [[0 for x in range(height)] for x in range(width)]
        board[0][0] = 1
        board[1][1] = 1
        board[2][2] = 1
        board[3][3] = 1
        board[4][4] = 1

        self.initUI(parent, board)


    def initUI(self, parent, board):
        self.parent.title("Simple")
        for i, row in enumerate(board):
            for j,column in enumerate(row):
                if board[i][j] == 0:
                    L = tk.Label(parent, text='    ',bg='black')
                else:
                    L = tk.Label(parent, text='    ',bg='red')

                L.grid(row=i,column=j)


def main():
    root = tk.Tk()
    app = UI(root, 10, 10)
    root.mainloop()


if __name__ == '__main__':
    main()

