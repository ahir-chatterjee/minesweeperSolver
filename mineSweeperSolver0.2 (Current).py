##################################################################################################################

import random
import time

class Field():

    def __init__(self,rowSize,colSize,value):
        self.board = [[value for x in range(rowSize)] for y in range(colSize)]
        self.rowSize = rowSize
        self.colSize = colSize
        self.size = rowSize*colSize

    def inBounds(self, row, col):
        if(row < 0):
            return False
        if(row >= self.rowSize):
            return False
        if(col < 0):
            return False
        if(col >= self.colSize):
            return False
        return True

    def printBoard(self):
        print ""
        print "      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15"
        num = 0
        for row in self.board:
            if(num < 10):
                print "  " + (str)(num) + " ",
            else:
                print " " + (str)(num) + " ",
            for col in row:
                if (len((str)(col)) == 1):
                    print " " + (str)(col) + " ",
                elif (len((str)(col)) == 2):
                    print " " + (str)(col),
                elif (len((str)(col)) == 3):
                    print (str)(col),
                elif (len((str)(col)) > 3):
                    print (str)(round(col, 1)),
            num += 1
            print ""
        print ""

    def returnBoard(self):
        returnString = "\n"
        returnString += "      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15\n"
        num = 0
        for row in self.board:
            if(num < 10):
                returnString += "  " + (str)(num) + " "
            else:
                returnString += " " + (str)(num) + " "
            for col in row:
                if (len((str)(col)) == 1):
                    returnString += " " + (str)(col) + " "
                elif (len((str)(col)) == 2):
                    returnString += " " + (str)(col)
                elif (len((str)(col)) == 3):
                    returnString += (str)(col)
                elif (len((str)(col)) > 3):
                    returnString += (str)(round(col, 1))
            num += 1
            returnString += "\n"
        returnString += "\n"
        return returnString

class GameField(Field):

    def __init__(self,rowSize,colSize,bombs):
        Field.__init__(self,rowSize,colSize,0)
        self.numBombs = bombs
        num = 0
        field = open("field.txt",'w')
        print "field.txt imported."
        while True:
            rand = random.randint(0,(rowSize*colSize)-1)
            row = rand/rowSize
            col = rand - (row*colSize)
            if (self.board[row][col] == 0): #add in the bombs
                self.board[row][col] = 'B'
                num += 1
            if (num == bombs):
                break
        for row in range(0,rowSize):
            for col in range(0,colSize):
                if (self.board[row][col] == 0):
                    count = 0
                    if (self.inBounds(row,col+1)):
                        if (self.board[row][col+1] == 'B'):
                            count += 1
                    if (self.inBounds(row,col-1)):
                        if (self.board[row][col-1] == 'B'):
                            count += 1
                    if (self.inBounds(row+1,col+1)):
                        if (self.board[row+1][col+1] == 'B'):
                            count += 1
                    if (self.inBounds(row-1,col+1)):
                        if (self.board[row-1][col+1] == 'B'):
                            count += 1
                    if (self.inBounds(row-1,col)):
                        if (self.board[row-1][col] == 'B'):
                            count += 1
                    if (self.inBounds(row-1,col-1)):
                        if (self.board[row-1][col-1] == 'B'):
                            count += 1
                    if (self.inBounds(row+1,col-1)):
                        if (self.board[row+1][col-1] == 'B'):
                            count += 1
                    if (self.inBounds(row+1,col)):
                        if (self.board[row+1][col] == 'B'):
                            count += 1
                    self.board[row][col] = count
        for row in self.board:
            string = ""
            for char in row:
                string += (str)(char)
            field.write(string + '\n')
        field.close()
        print "field.txt made"
        
class GuessField(Field):

    def __init__(self,rowSize,colSize):
        Field.__init__(self,rowSize,colSize,'?')

    def flag(self,coord):
        coord.update('F')

    def tap(self,coord):
        if (gameField.board[coord.row][coord.col] == 'B'):
            print "GAME OVER"
            return True
        else:
            guessField.board[coord.row][coord.col] = gameField.board[coord.row][coord.col]
            return False

    def getUnturned(self):
        count = 0
        for row in self.board:
            for char in row:
                if (char == '?'):
                    count += 1
        return count

class CalcField(Field):

    def __init__(self,rowSize,colSize):
        Field.__init__(self,rowSize,colSize,0.0)

class Coord():

    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.value = guessField.board[row][col]
        self.prob = calcField.board[row][col]

    def getValue(self):
        return guessField.board[self.row][self.col]

    def getProb(self):
        return calcField.board[self.row][self.col]

    def touchingUnmarked(self):
        coords = []
        if (guessField.inBounds(self.row,self.col+1)):#0,1
            if (guessField.board[self.row][self.col+1] == '?'):
                coords.append(Coord(self.row,self.col+1))
        if (guessField.inBounds(self.row,self.col-1)):#0,-1
            if (guessField.board[self.row][self.col-1] == '?'):
                coords.append(Coord(self.row,self.col-1))
        if (guessField.inBounds(self.row+1,self.col+1)):#1,1
            if (guessField.board[self.row+1][self.col+1] == '?'):
                coords.append(Coord(self.row+1,self.col+1))
        if (guessField.inBounds(self.row-1,self.col+1)):#-1,1
            if (guessField.board[self.row-1][self.col+1] == '?'):
                coords.append(Coord(self.row-1,self.col+1))
        if (guessField.inBounds(self.row-1,self.col)):#-1,0
            if (guessField.board[self.row-1][self.col] == '?'):
                coords.append(Coord(self.row-1,self.col))
        if (guessField.inBounds(self.row-1,self.col-1)):#-1,-1
            if (guessField.board[self.row-1][self.col-1] == '?'):
                coords.append(Coord(self.row-1,self.col-1))
        if (guessField.inBounds(self.row+1,self.col-1)):#1,-1
            if (guessField.board[self.row+1][self.col-1] == '?'):
                coords.append(Coord(self.row+1,self.col-1))
        if (guessField.inBounds(self.row+1,self.col)):#1,0
            if (guessField.board[self.row+1][self.col] == '?'):
                coords.append(Coord(self.row+1,self.col))
        return coords

    def bombsTouching(self):
        count = 0
        if (guessField.inBounds(self.row,self.col+1)):#0,1
            if (guessField.board[self.row][self.col+1] == 'F'):
                count += 1
        if (guessField.inBounds(self.row,self.col-1)):#0,-1
            if ((guessField.board[self.row][self.col-1] == 'F')):
                count += 1
        if (guessField.inBounds(self.row+1,self.col+1)):#1,1
            if ((guessField.board[self.row+1][self.col+1] == 'F')):
                count += 1
        if (guessField.inBounds(self.row-1,self.col+1)):#-1,1
            if ((guessField.board[self.row-1][self.col+1] == 'F')):
                count += 1
        if (guessField.inBounds(self.row-1,self.col)):#-1,0
            if ((guessField.board[self.row-1][self.col] == 'F')):
                count += 1
        if (guessField.inBounds(self.row-1,self.col-1)):#-1,-1
            if ((guessField.board[self.row-1][self.col-1] == 'F')):
                count += 1
        if (guessField.inBounds(self.row+1,self.col-1)):#1,-1
            if ((guessField.board[self.row+1][self.col-1] == 'F')):
                count += 1
        if (guessField.inBounds(self.row+1,self.col)):#1,0
            if ((guessField.board[self.row+1][self.col] == 'F')):
                count += 1
        return count

    def update(self,value):
        self.value = value
        guessField.board[self.row][self.col] = value

    def setProb(self,prob):
        self.prob = prob
        calcField.board[self.row][self.col] = prob

    def updateProb(self):
        row = self.row
        col = self.col
        coords = []
        if (guessField.inBounds(self.row,self.col+1)):#0,1
            coords.append(Coord(row,col+1))
        if (guessField.inBounds(self.row,self.col-1)):#0,-1
            coords.append(Coord(row,col-1))
        if (guessField.inBounds(self.row+1,self.col+1)):#1,1
            coords.append(Coord(row+1,col+1))
        if (guessField.inBounds(self.row-1,self.col+1)):#-1,1
            coords.append(Coord(row-1,col+1))
        if (guessField.inBounds(self.row-1,self.col)):#-1,0
            coords.append(Coord(row-1,col))
        if (guessField.inBounds(self.row-1,self.col-1)):#-1,-1
            coords.append(Coord(row-1,col-1))
        if (guessField.inBounds(self.row+1,self.col-1)):#1,-1
            coords.append(Coord(row+1,col-1))
        if (guessField.inBounds(self.row+1,self.col)):#1,0
            coords.append(Coord(row+1,col))
        nearZero = False
        nearValue = False
        largestProb = 0.0
        for coord in coords:
            probBomb = 0.0
            if (coord.getValue() != '?' and coord.getValue() != 'F'):
                probBomb = (float)(coord.getValue())-(float)(coord.bombsTouching())
                if(probBomb == 0.0):
                    nearZero = True
                if(probBomb == (float)(len(coord.touchingUnmarked()))):
                    largestProb = 1.0
                probBomb = probBomb/(float)(len(coord.touchingUnmarked()))
                nearValue = True
                if(probBomb > largestProb):
                    largestProb = probBomb
        if(nearZero):
            calcField.board[self.row][self.col] = 0.0
        elif(nearValue):
            calcField.board[self.row][self.col] = largestProb
        if(largestProb == 1.0):
            calcField.board[self.row][self.col] = largestProb        

    def printProb(self):
        row = self.row
        col = self.col
        coords = []
        if (guessField.inBounds(self.row,self.col+1)):#0,1
            coords.append(Coord(row,col+1))
        if (guessField.inBounds(self.row,self.col-1)):#0,-1
            coords.append(Coord(row,col-1))
        if (guessField.inBounds(self.row+1,self.col+1)):#1,1
            coords.append(Coord(row+1,col+1))
        if (guessField.inBounds(self.row-1,self.col+1)):#-1,1
            coords.append(Coord(row-1,col+1))
        if (guessField.inBounds(self.row-1,self.col)):#-1,0
            coords.append(Coord(row-1,col))
        if (guessField.inBounds(self.row-1,self.col-1)):#-1,-1
            coords.append(Coord(row-1,col-1))
        if (guessField.inBounds(self.row+1,self.col-1)):#1,-1
            coords.append(Coord(row+1,col-1))
        if (guessField.inBounds(self.row+1,self.col)):#1,0
            coords.append(Coord(row+1,col))
        nearZero = False
        nearValue = False
        largestProb = 0.0
        for coord in coords:
            coord.printCoord()
            probBomb = 0.0
            if (coord.getValue() != '?' and coord.getValue() != 'F'):
                probBomb = (float)(coord.getValue())-(float)(coord.bombsTouching())
                print coord.getValue()
                print coord.bombsTouching()
                print (float)(coord.getValue())-(float)(coord.bombsTouching())
                print (float)(len(coord.touchingUnmarked()))
                if(probBomb == 0.0):
                    print "This is near a 0"
                    nearZero = True
                if(probBomb == (float)(len(coord.touchingUnmarked()))):
                    print "This should've assigned 1.0"
                    largestProb = 1.0
                probBomb = probBomb/(float)(len(coord.touchingUnmarked()))
                nearValue = True
                if(probBomb > largestProb):
                    print "probBomb became largestProb"
                    largestProb = probBomb
            #print probBomb
        print largestProb
        print nearZero
        print nearValue
        if(nearZero):
            calcField.board[self.row][self.col] = 0.0
        elif(nearValue):
            calcField.board[self.row][self.col] = largestProb
            print calcField.board[self.row][self.col]
            print Coord(self.row,self.col).getProb()

    def isSame(self,other):
        if (self.row == other.row and self.col == other.col):
            return True
        return False

    def printCoord(self):
        print "(" + (str)(self.row) + "," + (str)(self.col) + ")"

    def returnCoord(self):
        return "(" + (str)(self.row) + "," + (str)(self.col) + ")"

##################################################################################################################

#STATIC VARIABLES
bombs, rowSize, colSize = 40, 16, 16
#STATIC VARIABLES

gameField = GameField(rowSize,colSize,bombs)
gameField.returnBoard()

##################################################################################################################

##################################################################################################################

############################################INITIAL###############################################################

guessField = GuessField(rowSize,colSize)
calcField = CalcField(rowSize,colSize)

remaining = bombs
baseProb = (float)(remaining)/guessField.getUnturned()
zeros = []
ones = []
unknowns = []
gameOver = False
log = open("log.txt",'w')
print "log.txt imported."

for row in range(0,len(guessField.board)):
    for col in range(0,len(guessField.board[0])):
        calcField.board[row][col] = baseProb
        unknowns.append(Coord(row,col))
print len(unknowns)

while(remaining != 0 and gameOver != True):
    ############################################PRIOR#################################################################
    
    flagged = False
    choice = Coord(0,0)
    if(len(ones) != 0):
        choice = ones.pop()
        log.write("flagged" + choice.returnCoord() + "\n")
        print "flagged" + choice.returnCoord()
        guessField.flag(choice) #deposits a flag
        remaining -= 1
        flagged = True
    elif(len(zeros) != 0):
        choice = zeros.pop()
        log.write("safe tap" + choice.returnCoord() + "\n")
        print "safe tap" + choice.returnCoord()
        if(guessField.tap(choice)): #taps a square, returns either game over or updates the board
            gameField.returnBoard()
            guessField.returnBoard()
            calcField.returnBoard()
            gameField.printBoard()
            guessField.printBoard()
            calcField.printBoard()
            break
    else:
        for coord in unknowns:
            if (coord.getProb() < choice.getProb() or choice.getValue() != '?'):
                choice = coord
        for coord in unknowns:
            if (coord.isSame(choice)):
                print unknowns.pop(unknowns.index(coord))
        log.write("random tap" + choice.returnCoord() + "\n")
        print "random tap" + choice.returnCoord()
        if(guessField.tap(choice)): #taps a square, returns either game over or updates the board
            gameField.returnBoard()
            guessField.returnBoard()
            calcField.returnBoard()
            gameField.printBoard()
            guessField.printBoard()
            calcField.printBoard()
            break

    ###############################################EVIDENCE###########################################################

    #This step is done automatically by the individual classes based off what happens in PRIOR

    ##################################################POSTERIOR#######################################################
    if(not flagged):
        choice.setProb('X')
    coords = choice.touchingUnmarked() #these are all coordinates affected by the chosen coordinate
    for coord in coords:
        log.write(coord.returnCoord() + "\n")
    #coords.append(choice)
    for coord in coords:
        coord.updateProb()
    for coord in unknowns:
        if(coord.getProb() == 1.0):
            ones.append(coord)
            for coord in unknowns:
                if (coord.isSame(choice)):
                    print unknowns.pop(unknowns.index(coord))
        elif(coord.getProb() == 0.0):
            zeros.append(coord)
            for coord in unknowns:
                if (coord.isSame(choice)):
                    print unknowns.pop(unknowns.index(coord))
    '''unknownSum = 0.0
    for coord in unknowns:
        unknownSum += coord.getProb()
    if(unknownSum == 0):
        gameField.returnBoard()
        guessField.returnBoard()
        calcField.returnBoard()
        gameField.printBoard()
        guessField.printBoard()
        calcField.printBoard()
        break
    scalar = (float)(remaining)/(float)(unknownSum)
    for coord in unknowns:
        coord.setProb(coord.getProb()*scalar)'''

    #guessField.printBoard()
    #calcField.printBoard()
    log.write(guessField.returnBoard())
    log.write(calcField.returnBoard())

if(remaining == 0):
    "WIN!"

print len(unknowns)
guessField.printBoard()
calcField.printBoard()
print "Bombs Remaining: " + (str)(remaining)
Coord((int)(raw_input("Row: ")),int(raw_input("Col: "))).printProb()


