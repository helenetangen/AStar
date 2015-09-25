__author__ = 'helenetangen'



class Board:
    def makeBoard(self, height, width):
        board = [[0 for x in range(height)] for x in range(width)]
        return board


class Node:
    def __init__(self,parent,state,g,h):
        self.parent=parent
        self.state = state
        self.g=g
        self.h=h
        self.f=g + h
        self.children = []


class Search:

    board  = [[0,0,0,1,1],
              [0,0,0,1,1],
              [0,0,0,0,0],
              [1,1,1,0,0],
              [0,0,0,0,0]]
    open   = [] #Sort open
    closed = []


    def manhattan(self, start, end):
        return (end[0] - start[0]) + (end[1] - start[1])
    
    def search(self, start, end):
        h    = self.manhattan(start, end)
        node = Node(None, start, 0, h)
        self.open.append(node)
       

        while(node.state != end):
            if (len(self.open) == 0):
                print "Failed. No nodes in open."
                return
            node = self.open.pop(0)   # X - Best Node in open
            print "popped!"
            self.closed.append(node)
            if (node.state==end):
                print "You got it!"
                return
        children = getChildren()
        for child in children:
            
            















def main():
    s = Search()
    s.search((1,1), (2,2))


if __name__ == '__main__':
    main()
