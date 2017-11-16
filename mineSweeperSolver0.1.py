import random
import time

field = open("field.txt",'w')
print "field.txt imported."

#STATIC VARIABLES
bombs, size = 40, 16
#STATIC VARIABLES

def inBounds(row, col):
    if(row < 0):
        return False
    if(row >= size):
        return False
    if(col < 0):
        return False
    if(col >= size):
        return False
    return True

def printField(field):
    print ""
    print "      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15"
    num = 0
    for row in field:
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

gameField = [[0 for x in range(size)] for y in range(size)]

num = 0

while True:
    rand = random.randint(0,(size*size)-1)
    row = rand/16
    col = rand - (row*size)
    if (gameField[row][col] == 0):
        gameField[row][col] = 'B'
        num += 1
        print num
    if (num == bombs):
        break

for row in range(0,size):
    for col in range(0,size):
        if (gameField[row][col] == 0):
            count = 0
            if (inBounds(row,col+1)):
                if (gameField[row][col+1] == 'B'):
                    count += 1
            if (inBounds(row,col-1)):
                if (gameField[row][col-1] == 'B'):
                    count += 1
            if (inBounds(row+1,col+1)):
                if (gameField[row+1][col+1] == 'B'):
                    count += 1
            if (inBounds(row-1,col+1)):
                if (gameField[row-1][col+1] == 'B'):
                    count += 1
            if (inBounds(row-1,col)):
                if (gameField[row-1][col] == 'B'):
                    count += 1
            if (inBounds(row-1,col-1)):
                if (gameField[row-1][col-1] == 'B'):
                    count += 1
            if (inBounds(row+1,col-1)):
                if (gameField[row+1][col-1] == 'B'):
                    count += 1
            if (inBounds(row+1,col)):
                if (gameField[row+1][col] == 'B'):
                    count += 1
            gameField[row][col] = count

for row in gameField:
    string = ""
    for char in row:
        string += (str)(char)
    field.write(string + '\n')

field.close()
print "field.txt made"
printField(gameField)
#time.sleep(5)



##################################################################################################################

def countUnturned(row, col): #determines how many unturned tiles a tile touches and returns an int
    count = 0
    if (inBounds(row,col+1)):
        if (calcField[row][col+1] != 'X'):
            count += 1
    if (inBounds(row,col-1)):
        if (calcField[row][col-1] != 'X'):
            count += 1
    if (inBounds(row+1,col+1)):
        if (calcField[row+1][col+1] != 'X'):
            count += 1
    if (inBounds(row-1,col+1)):
        if (calcField[row-1][col+1] != 'X'):
            count += 1
    if (inBounds(row-1,col)):
        if (calcField[row-1][col] != 'X'):
            count += 1
    if (inBounds(row-1,col-1)):
        if (calcField[row-1][col-1] != 'X'):
            count += 1
    if (inBounds(row+1,col-1)):
        if (calcField[row+1][col-1] != 'X'):
            count += 1
    if (inBounds(row+1,col)):
        if (calcField[row+1][col] != 'X'):
            count += 1
    return count

def countTotal(row, col): #determines how many total tiles a tile touches and returns an int
    count = 0
    if (inBounds(row,col+1)):
            count += 1
    if (inBounds(row,col-1)):
            count += 1
    if (inBounds(row+1,col+1)):
            count += 1
    if (inBounds(row-1,col+1)):
            count += 1
    if (inBounds(row-1,col)):
            count += 1
    if (inBounds(row-1,col-1)):
            count += 1
    if (inBounds(row+1,col-1)):
            count += 1
    if (inBounds(row+1,col)):
            count += 1
    return count

def touchesTurned(row, col): #determines if a tile touches a turned tile and returns a list of row | col pairs
    coords = []
    if (inBounds(row,col+1)):
        if (calcField[row][col+1] == 'X'):
            coords.append(row)
            coords.append(col+1)
    if (inBounds(row,col-1)):
        if (calcField[row][col-1] == 'X'):
            coords.append(row)
            coords.append(col-1)
    if (inBounds(row+1,col+1)):
        if (calcField[row+1][col+1] == 'X'):
            coords.append(row+1)
            coords.append(col+1)
    if (inBounds(row-1,col+1)):
        if (calcField[row-1][col+1] == 'X'):
            coords.append(row-1)
            coords.append(col+1)
    if (inBounds(row-1,col)):
        if (calcField[row-1][col] == 'X'):
            coords.append(row-1)
            coords.append(col)
    if (inBounds(row-1,col-1)):
        if (calcField[row-1][col-1] == 'X'):
            coords.append(row-1)
            coords.append(col-1)
    if (inBounds(row+1,col-1)):
        if (calcField[row+1][col-1] == 'X'):
            coords.append(row+1)
            coords.append(col-1)
    if (inBounds(row+1,col)):
        if (calcField[row+1][col] == 'X'):
            coords.append(row+1)
            coords.append(col)
    return coords

def touchesZero(row, col):
    if (inBounds(row,col+1)):
        if (guessField[row][col+1] == 0):
            return True
    if (inBounds(row,col-1)):
        if (guessField[row][col-1] == 0):
            return True
    if (inBounds(row+1,col+1)):
        if (guessField[row+1][col+1] == 0):
            return True
    if (inBounds(row-1,col+1)):
        if (guessField[row-1][col+1] == 0):
            return True
    if (inBounds(row-1,col)):
        if (guessField[row-1][col] == 0):
            return True
    if (inBounds(row-1,col-1)):
        if (guessField[row-1][col-1] == 0):
            return True
    if (inBounds(row+1,col-1)):
        if (guessField[row+1][col-1] == 0):
            return True
    if (inBounds(row+1,col)):
        if (guessField[row+1][col] == 0):
            return True
    return False

def testProbability(row,col):
    coords = touchesTurned(row,col)
    if (coords): #if tile touches turned tiles... (below is shaky code)
        chance = 1.0
        for num in range(0,len(coords)/2): #count bombs touched by spaces touched and figure out the highest bomb number around it (for now)
            count = 0
            bombsTouched = 0
            r = (int)(coords[count])
            c = (int)(coords[count+1])
            oCoords = touchesTurned(r,c)
            print ((str)(r) + " " + (str)(c) + ": "),
            print oCoords
            for num in range(0,len(oCoords)/2):
                row = num + count
                col = num + count + 1
                if (guessField[row][col] == 'B'):
                    bombsTouched += 1
                count += 2
                print (str)(row) + " " + (str)(col)
                if(chance > ((float)(guessField[row][col])-bombsTouched)/(float)(countUnturned(row,col))):
                    chance = ((float)(guessField[row][col])-bombsTouched)/(float)(countUnturned(row,col))
    print chance

##################################################################################################################

guessField = [['?' for x in range(size)] for y in range(size)]
calcField = [[0 for x in range(size)] for y in range(size)]

uCount = size*size
rBombs = bombs

############################################INITIAL###############################################################

guessField = guessField()
calcField = calcField()

remaining = bombs
baseProb = remaining/guessField.getUnturned()
zeros = []
ones = []
unknowns = []

while(remaining != 0):
    ############################################PRIOR#################################################################

    choice = Coords(0,0)
    if(len(ones) != 0):
        choice = ones.remove()
        guessField.flag(choice)
    elif(len(zeros) != 0):
        choice = zeros.remove()
        guessField.tap(choice)
    else:
        choice = min(unknowns)
        guessField.tap(choice)

    ###############################################EVIDENCE###########################################################

    #This step is done automatically by the individual classes based off what happens in PRIOR

    ##################################################POSTERIOR#######################################################

    coords = choice.touchingUnmarked() #these are all coordinates affected by the chosen coordinate
    
        

for number in range(0,(size*size)-1):
    #assess possibility of each tile -being a bomb
    uChance = (float)(rBombs)/(float)(size*size)
    for row in range(0,size):
        for col in range(0,size):
            if (guessField[row][col] == '?'): #if tile is unturned...
                coords = touchesTurned(row,col)
                if (coords): #if tile touches turned tiles... (below is shaky code)
                    chance = 1.0
                    for num in range(0,len(coords)/2): #count bombs touched by spaces touched and figure out the highest bomb number around it (for now)
                        count = 0
                        bombsTouched = 0
                        r = (int)(coords[count])
                        c = (int)(coords[count+1])
                        oCoords = touchesTurned(r,c)
                        for num in oCoords:
                            if (guessField[r][c] == 'B'):
                                bombsTouched += 1
                            count += 2
                        if(chance > ((float)(guessField[r][c])-bombsTouched)/(float)(countUnturned(r,c))):
                            chance = ((float)(guessField[r][c])-bombsTouched)/(float)(countUnturned(r,c))
                    r = coords[0]
                    c = coords[1]
                    if(guessField[r][c] != 'B'):
                        calcField[row][col] = chance
                    numCoords = len(coords)/2
                else: #if no extra information assign uChance
                    calcField[row][col] = uChance
                if (touchesZero(row, col)):
                    calcField[row][col] = 0 
    #choose lowest probability of being a bomb
    cRow = size/2
    cCol = size/2
    for row in range(0,size):
        for col in range(0,size):
            if (calcField[cRow][cCol] == 'X'):
                cRow = row
                cCol = col
            if (calcField[row][col] < calcField[cRow][cCol]):
                cRow = row
                cCol = col
                print "(" + (str)(cRow) + " ," + (str)(cCol) + ")"
            if (calcField[row][col] >= 1 and calcField[row][col] != 'X' and guessField[row][col] != 'B'):
                guessField[row][col] = 'B'
                rBombs -= 1
    #update all fields with choices
    if(gameField[cRow][cCol] == 'B'):
        print "Game Over"
        printField(calcField)
        break
    calcField[cRow][cCol] = 'X'
    guessField[cRow][cCol] = gameField[cRow][cCol]
    #printField(gameField)
    #printField(guessField)
    #printField(calcField)
    #time.sleep(3)
    #check for any confirmed bombs

def commands(cmd):
    cmdarray = cmd.split()
    if (cmdarray[0] == "touchesTurned"):
        print touchesTurned((int)(cmdarray[1]),(int)(cmdarray[2]))
    elif (cmdarray[0] == "countUnturned"):
        print countUnturned((int)(cmdarray[1]),(int)(cmdarray[2]))
    elif (cmdarray[0] == "getCoord"):
        r = (int)(cmdarray[1])
        c = (int)(cmdarray[2])
        print "gameField: " + (str)(gameField[r][c])
        print "guessField: " + (str)(guessField[r][c])
        print "calcField: " + (str)(calcField[r][c])
    elif (cmdarray[0] == "numBombs"):
        print rBombs
    elif (cmdarray[0] == "printFields"):
        printField(gameField)
        printField(guessField)
        printField(calcField)
    elif (cmdarray[0] == "testProbability"):
        testProbability((int)(cmdarray[1]), (int)(cmdarray[2]))
    else:
        print "Try again."

while True:
    print "Enter command (touchesTurned, countUnturned, getCoord, numBombs, printFields, testProbability)."
    cmd = raw_input("")
    if (cmd == "close"):
        break
    print ""
    commands(cmd)
    
