__author__ = 'helenetangen and jean'


class Node:


    def __init__(self,parent,x,y,g,h):
        self.parent = parent
        self.x = x
        self.y = y
        self.g = g      #Cost of getting from start to current state
        self.h = h      #Cost of getting to goal state from current state
        self.f = g + h  #Estimated total path cost
        self.children = []
        self.closed=False


    def setParent(self,parent):
        self.parent=parent


    def setG(self,g):
        self.g=g


    def setH(self,h):
        self.h=h


    def setF(self):
        self.f=self.g+self.h


    def close(self):
        self.closed=True
        


class Search:


    open   = []
    closed = []
    dictionary = {}


    def __init__(self, size, start_x, start_y, goal_x, goal_y, barriers):
        self.size    = size
        self.start_x = start_x
        self.start_y = start_y
        self.goal_x  = goal_x
        self.goal_y  = goal_y
        self.board   = [[]]
        self.make_board(self.size, barriers)


    def print_open(self):
        for node in self.open:
            print "(" + str(node.x) + ", " + str(node.y) + ")"


    def propagate_path_improvement(self, parent):
        for child in parent.children:
            if parent.g + self.arc_cost() < child.g:
                child.parent = parent
                child.g = parent.g + self.arc_cost()
                child.f = child.g + child.h
                self.propagate_path_improvement(child)


    def arc_cost(self):
        return 1


    def make_board(self, size, barriers):
        self.board = [[0 for x in range(size)] for x in range(size)]
        #Add barriers
        for barrier in barriers:
            x = barrier[0]
            y = barrier[1]
            x_length = barrier[2]
            y_length = barrier[3]

            for i in range(x, x + x_length):
                for j in range(y, y + y_length):
                    self.board[i][j] = 1


    def print_board(self, board):
        print "-------------"
        for i in range(self.size):
            for j in range(self.size):
                print str(board[i][j]) + " ",
            print "\n"
        print "-------------"


    def print_board(self, board, x, y):
        print "-------------"
        for i in range(self.size):
            for j in range(self.size):
                if x == i and y == j:
                    print "x ",
                else:
                    print str(board[i][j]) + " ",
            print "\n"
        print "-------------"


    def manhattan(self, x, y):
        return (self.goal_x - x) + (self.goal_y - y)


    def generate_children(self, parent):
        children = []

        x = parent.x + 1
        y = parent.y
        if parent.x + 1 < self.size and self.board[x][y] == 0:
            child = Node(parent, x, y, parent.g + self.arc_cost(), self.manhattan(x, y))
            children.append(child)

        x = parent.x - 1
        y = parent.y
        if parent.x + 1 < 0 and self.board[x][y] == 0:
            child = Node(parent, x, y, parent.g + self.arc_cost(), self.manhattan(x, y))
            children.append(child)

        x = parent.x
        y = parent.y + 1
        if parent.y + 1 < self.size and self.board[x][y] == 0:
            child = Node(parent, x, y, parent.g + self.arc_cost(), self.manhattan(x, y))
            children.append(child)

        x = parent.x
        y = parent.y - 1
        if parent.x + 1 < 0 and self.board[x][y] == 0:
            child = Node(parent, x, y, parent.g + self.arc_cost(), self.manhattan(x, y))
            children.append(child)

        return children


    # AGENDA LOOP
    def search(self):

        #Make initial node
        node = Node(None, self.start_x, self.start_y, 0, self.manhattan(self.start_x, self.start_y))
        self.open.append(node)
        self.dictionary[str(node.x) + "-" + str(node.y)] = node

        #Search for solution
        while not (node.x == self.goal_x and node.y == self.goal_y):

            #Check if the solution exist
            if (len(self.open) == 0):
                print "Failed. No nodes in open."
                return

            #Print open
            self.print_open()

            #Get current best search state to search from
            node = self.open.pop(0)   # X = Top Node in sorted open
            node.close()
            self.closed.append(node)

            #Print current board
            self.print_board(self.board, node.x, node.y)


            #Check if you have found the goal state
            if (node.x == self.goal_x and node.y == self.goal_y):
                print "You got it!"
                return

            children = self.generate_children(node)
                         
            for child in children:

                id = str(child.x) + "-" + str(child.y)
                if (id in self.dictionary.keys()):
                    child = self.dictionary.get(id)
                         
                node.children.append(child)


                if not (id in self.dictionary):
                         self.open.append(child)
                         self.dictionary[str(child.x) + "-" + str(child.y)] = child
                         #self.open = sorted(self.open, key=lambda Node : Node.f)
                else:
                    if node.g + self.arc_cost() < child.g:
                        child.setParent(node)
                        child.setG(node.g + self.arc_cost)
                        child.setF()
                        if (child.closed):
                            self.propagate_path_improvement(child)


def main():
    search = Search(5, 0, 0, 4, 4, [[3, 0, 1, 3],[0, 3, 2, 2]])
    search.search()


if __name__ == '__main__':
    main()
