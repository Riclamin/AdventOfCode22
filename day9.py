
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = [(x,y)]
    
    def __repr__(self):
        return f'({self.x},{self.y})'

    def updateHistory(self):
        self.history.append((self.x,self.y))

    
    def shiftRight(self):
        self.x +=1
        self.updateHistory()

    def shiftLeft(self):
        self.x -=1
        self.updateHistory()
    
    def shiftUp(self):
        self.y +=1
        self.updateHistory()
    
    def shiftDown(self):
        self.y -=1
        self.updateHistory()

    def shiftUpRight(self):
        self.x +=1
        self.y +=1
        self.updateHistory()

    def shiftUpLeft(self):
        self.x -=1
        self.y +=1
        self.updateHistory()
    
    def shiftDownRight(self):
        self.x +=1
        self.y -=1
        self.updateHistory()
    
    def shiftDownLeft(self):
        self.x -=1
        self.y -=1
        self.updateHistory()
    
    def followPoint(self, other):

        # check if we need to move diagonally
        if (abs(other.x - self.x) + abs(other.y - self.y)) > 2 :
            if other.x - self.x >= 1:
                if other.y - self.y >= 1:
                    self.shiftUpRight()
                elif other.y - self.y <= -1:
                    self.shiftDownRight()

            elif other.x - self.x <= -1:
                if other.y - self.y >= 1:
                    self.shiftUpLeft()
                elif other.y - self.y <= -1:
                    self.shiftDownLeft()

        else: # we can move orthogonally
            if other.x - self.x > 1:
                self.shiftRight()
            elif other.x - self.x < -1:
                self.shiftLeft()
            elif other.y - self.y > 1:
                self.shiftUp()
            elif other.y - self. y < -1:
                self.shiftDown()

        

class knot:
    def __init__(self, x , y, knots):
        self.knots = []
        for _ in range (knots):
            self.knots.append(point(x,y))
        print(len(self.knots))
    
    def shiftHead(self, direction):
        split = direction.split(' ')
        orientation = split[0]
        length = int(split[1])
        while length > 0:
            length -=1
            if orientation == 'R':
                self.knots[0].shiftRight()
            elif orientation == 'L':
                self.knots[0].shiftLeft()
            elif orientation == 'U':
                self.knots[0].shiftUp()
            elif orientation == 'D':
                self.knots[0].shiftDown()
            
            for k in range(1, len(self.knots)):
                self.knots[k].followPoint(self.knots[k-1])



    




Example = "./Input/Example9.txt"
Example2= "./Input/Example9_2.txt"
Input = "./Input/Input9.txt"

f = open(Input, 'r')



# part 1

lines = f.readlines()

knots = knot(0,0, 10)

# Check visibility in rows.
for line in lines:
    line = line.strip('\n')
    knots.shiftHead(line)

print(len(set(knots.knots[-1].history)))


# Parsed all input/output

