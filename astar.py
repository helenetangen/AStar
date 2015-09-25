__author__ = 'helenetangen'


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
        self.board   = [[]]
        self.make_board(self.size, barriers)


    def make_board(self, size, barriers):
        board = [[0 for x in range(size)] for x in range(size)]
        #Add barriers
        for barrier in barriers:
            x = barrier[0]
            y = barrier[1]
            x_length = barrier[2]
            y_length = barrier[3]

            for i in range(x, x + x_length):
                for j in range(y, y + y_length):
                    board[i][j] = 1
        print self.print_board(board)



    def print_board(self, board):
        print "-------------"
        for i in range(self.size):
            for j in range(self.size):
                print str(board[i][j]) + " ",
            print "\n"
        print "-------------"

    
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


    '''
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
                         
            children = self.generate_children()
            for child in children:
            
            else:
                node = self.open.pop(0)
                self.closed.append(node)
    '''


def main():
    search = Search(5, 0, 0, 4, 4, [[3, 0, 1, 3],[0, 3, 2, 2]])


if __name__ == '__main__':
    main()
