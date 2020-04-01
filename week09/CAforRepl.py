#we need random numbers
import random

#only for repl.it
#for clearing the screen and slowing down our program
import replit 
import time

#utility for building a 2D matrix full of zeroes
def generate(matrix):
    #loop once per requested row
    for row in range (rowCount):
        #add a row
        matrix.append([])
        #loop once per requested row
        for col in range (colCount):
            #add a zero in each cell
            matrix[row].append(0)

#utility for printing 2D matrices cleanly             
def printWorld(matrix):
    #look at each row
    for row in matrix:
	    #look at each column in the row
        for col in row:
	        #print the cell, and a following space
            print(col, end=" ")
	    # Add a new line after each row
        print()
      
#utility for randomly filling a 2D matrix   
def populate(matrix, livingCount):
    #loop once per requested living cell
    for i in range (livingCount):
        #generate random coordinate for bringing cells to life
        row = random.randint(0,rowCount - 1)
        col = random.randint(0,colCount - 1)
        #set random cell to living
        matrix[row][col] = 1

#rules and settings
#for predictable randomness
random.seed(3)

#0->8 inclusive need to be share between these two arrays
#which neighbor counts animate a dead cell?
ZeroToOne = [3]
#which neighbor counts leave a cell dead?
ZeroToZero = [0,1,2,4,5,6,7,8]

#0->8 inclusive need to be share between these two arrays
#which neighbor counts kill a living cell?
OneToZero = [0,1,4,5,6,7,8]
#which neighbor counts keep a cell alive?
OneToOne = [2,3]



#world settings
colCount = 10
rowCount = 7
startingPop = 30

#how many generations
gen = 5 

#empty matrices for later use
#hold current state
world = []
#matrix to hold next state while it is being built
newWorld = []



#fill matrix with zeroes
generate(world)
#randomly add population
populate(world, startingPop)



#loop through generations, starting at 1 since we have a zeroeth generation already
for g in range(1, gen+1):
    #loop through each row
    for row in range (rowCount):
        #add an empty row to our next generation
        newWorld.append([])
        #loop through each column
        for col in range (colCount):
            
            #check if top neighbor is alive
            if (row - 1 < 0):
                topNB = 0
            else:   
                topNB = world[row - 1][col]
            
            #check if bottom neighbor is alive
            if (row + 1 == rowCount):
                bottomNB = 0
            else:
                bottomNB = world[row + 1][col]
            
            #check if left neighbor is alive
            if (col - 1 < 0):
                leftNB = 0
            else:
                leftNB = world[row][col-1] 
            
            #check if right neighbor is alive
            if (col + 1 == colCount):
                rightNB = 0
            else:
                rightNB = world[row][col+1]
            
            #check if upper left neighbor is alive
            if (row - 1 < 0) or (col - 1 < 0):
                tlNB = 0
            else:
                tlNB = world[row-1][col-1]
           
            #check if bottom left neighbor is alive
            if (row + 1 == rowCount) or (col - 1 < 0):
                blNB = 0
            else:
                blNB = world[row+1][col-1]
            
            #check if top right neighbor is alive
            if (row - 1 < 0) or (col + 1 == colCount):
                trNB = 0
            else:
                trNB = world[row-1][col+1]
            
            #check if bottom right neighbor is alive
            if (row + 1 == rowCount) or (col + 1 == colCount):
                brNB = 0
            else:
                brNB = world[row+1][col+1]
            
            #record if this cell alive or dead
            currentCell = world[row][col]

            #how many of our neighbors are alive?
            neighborLife = leftNB + rightNB + topNB + bottomNB + brNB + trNB + tlNB + blNB

            # current cell is alive...
            if currentCell == 1 :      
                #what should happen in the next generation?    
                if neighborLife in OneToZero:
                    newWorld[row].append(0)
                elif neighborLife in OneToOne:
                    newWorld[row].append(1)
            
            # current cell is dead...
            else :  
                #what should happen in the next generation?    
                if neighborLife in ZeroToZero:
                    newWorld[row].append(0)
                elif neighborLife in ZeroToOne:
                    newWorld[row].append(1)
    
    #see next generation
    printWorld(newWorld)
    #wait one second
    time.sleep(1)
    #clear screen
    replit.clear()

    #update our world 
    world = newWorld
    #erase newWorld so it is ready for next generation
    newWorld = []

print('Done!')