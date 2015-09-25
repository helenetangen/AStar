__author__ = 'helenetangen'



class Board:
    def makeBoard(self, height, width):
        board = [[0 for x in range(height)] for x in range(width)]
        return board


class Node:
    def __init__(self,parent,x,y,g,h):
        self.parent = parent
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h
        self.children = []


class Search:


    open   = []
    closed = []


    def __init__(self, size, start_x, start_y, goal_x, goal_y, barriers):
        self.size    = size
        self.start_x = start_x
        self.start_y = start_y
        self.goal_x  = goal_x
        self.goal_y  = goal_y


    def make_board(self, size, barriers):
        board = [[0 for x in range(size)] for x in range(size)]
        #Add barriers

    
    def search(self, start, end):
        h    = self.manhattan(start, end)
        node = Node(None, start, 0, h)
        self.open.append(node)


    def manhattan(self, x, y):
        return (self.goal_x - x) + (self.goal_y - y)


    def generate_children(self, parent, size):
        children = []

        x = parent.x + 1
        y = parent.y
        if parent.x + 1 < size and self.board[x][y] == 0:
            child = Node(parent, x, y, parent.g + 1, self.manhattan(x, y))
            children.append(child)

        x = parent.x - 1
        y = parent.y
        if parent.x + 1 < 0 and self.board[x][y] == 0:
            child = Node(parent, x, y, parent.g + 1, self.manhattan(x, y))
            children.append(child)

        x = parent.x
        y = parent.y + 1
        if parent.y + 1 > size and self.board[x][y] == 0:
            child = Node(parent, x, y, parent.g + 1, self.manhattan(x, y))
            children.append(child)

        x = parent.x
        y = parent.y - 1
        if parent.x + 1 < 0 and self.board[x][y] == 0:
            child = Node(parent, x, y, parent.g + 1, self.manhattan(x, y))
            children.append(child)

        return children


    def search(self, start, end):
        h = self.manhattan(start, end)
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
            node = self.open.pop(0)
            self.closed.append(node)


                         
            children = generate_children()
            for child in children:
            
            else:
                node = self.open.pop(0)
                self.closed.append(node)



def main():
    s = Search()
    s.search((1,1), (2,2))


if __name__ == '__main__':
    main()