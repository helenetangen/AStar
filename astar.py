__author__ = 'helenetangen'



class Board:


    def makeBoard(self, height, width):
        board = [[0 for x in range(height)] for x in range(width)]
        return board

class Node:
    def __init__(self,parent,x,y,g,h):
        self.parent=parent
        self.x=x
        self.y=y
        self.g=g
        self.h=h
        self.children = []

<<<<<<< HEAD
=======

>>>>>>> 39319835a0068abf7a0b390a3ce198a2d9efb34c
def main():
    b = Board()
    b.board = b.makeBoard(5, 5)
    for i in range(5):
        b.board[i][i] = 1
<<<<<<< HEAD
        print b.board[i][i]
=======
       # print b.board[i][i]

    mynode = Node(None,0,0,0,0)
    print mynode.parent,mynode.children,mynode.Ch
>>>>>>> 39319835a0068abf7a0b390a3ce198a2d9efb34c


if __name__ == '__main__':
    main()
