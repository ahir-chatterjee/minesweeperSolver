import random

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

for row in range(0,size-1):
    for col in range(0,size-1):
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
            if (inBounds(row,col)):
                if (gameField[row][col] == 'B'):
                    count += 1
            gameField[row][col] = count

for row in gameField:
    string = ""
    for char in row:
        string += (str)(char)
    field.write(string + '\n')

field.close()
print "field.txt closed"










    
