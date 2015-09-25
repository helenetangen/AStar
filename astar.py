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

    board  = [[0,0,0,1,1],
              [0,0,0,1,1],
              [0,0,0,0,0],
              [1,1,1,0,0],
              [0,0,0,0,0]]
    open   = [] #Sort open
    closed = []
    goal_x = 4
    goal_y = 4


    def manhattan(self, start, end):
        return (end[0] - start[0]) + (end[1] - start[1])
    
    def search(self, start, end):
        h    = self.manhattan(start, end)
        node = Node(None, start, 0, h)
        self.open.append(node)
       
    def manhattan(self, node):
        return (self.goal_x - node.x) + (self.goal_y - node.y)


    def generate_children(self, parent, size):
        children = []

        x = parent.x + 1
        y = parent.y
        if parent.x + 1 < size:
            child = Node(parent, x, y, parent.g + 1, self.manhattan(x, y, self.goal_x, self.goal_y)
            children.append(child)

        x = parent.x - 1
        y = parent.y
        if parent.x + 1 < 0:
            child = Node(parent, x, y, parent.g + 1, self.manhattan(x, y, self.goal_x, self.goal_y)
            children.append(child)

        x = parent.x
        y = parent.y + 1
        if parent.y + 1 > size:
            child = Node(parent, x, y, parent.g + 1, self.manhattan(x, y, self.goal_x, self.goal_y)
            children.append(child)

        x = parent.x
        y = parent.y - 1
        if parent.x + 1 < 0:
            child = Node(parent, x, y, parent.g + 1, self.manhattan(x, y, self.goal_x, self.goal_y)
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
        children = getChildren()
        for child in children:
            
            
            else:
                node = self.open.pop(0)
                self.closed.append(node)



def main():
    s = Search()
    s.search((1,1), (2,2))


if __name__ == '__main__':
    main()
