#imports
import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
import random

#build empty matrix
def generate(matrix):
	for row in range (rowCount):
		matrix.append([])
		for col in range (colCount):
			matrix[row].append(0)

#randomly flip bits
def populate(matrix, living):
	points.append([])
	for i in range (living):
		row = random.randint(0,rowCount - 1)
		col = random.randint(0,colCount - 1)
		matrix[row][col] = 1
		points[0].append(rs.AddPoint(col,row,0))

#create structural matrices
world = []
newWorld = []
points = []

#world settings
random.seed(seed)
colCount = columns
rowCount = rows
pop = population
gen = generations 

#build world
generate(world)
#randomly populate world
populate(world, pop)

#iterate generations
for g in range(1,gen+1):
	#loop for each row
	points.append([])
	for row in range (rowCount):
		newWorld.append([])
		   
		#loop for each column
		for col in range (colCount):
			
			#living/dead checks
			if (row - 1 < 0):
				leftNB = 0
			else:   
				leftNB = world[row - 1][col]

			if (row + 1 == rowCount):
				rightNB = 0
			else:
				rightNB = world[row + 1][col]
			
			if (col - 1 < 0):
				topNB = 0
			else:
				topNB = world[row][col-1] 

			if (col + 1 == colCount):
				bottomNB = 0
			else:
				bottomNB = world[row][col+1]

			if (row - 1 < 0) or (col - 1 < 0):
				tlNB = 0
			else:
				tlNB = world[row-1][col-1]

			if (row + 1 == rowCount) or (col - 1 < 0):
				trNB = 0
			else:
				trNB = world[row+1][col-1]
			
			if (row - 1 < 0) or (col + 1 == colCount):
				blNB = 0
			else:
				blNB = world[row-1][col+1]
		
			if (row + 1 == rowCount) or (col + 1 == colCount):
				brNB = 0
			else:
				brNB = world[row+1][col+1]
			
			#get current state
			currentCell = world[row][col]
			#sum neighborhood
			neighborLife = leftNB + rightNB + topNB + bottomNB + brNB + trNB + tlNB + blNB
 
			# current cell is alive...
			if currentCell == 1 :
				#transitions
				if neighborLife in OneToZero:
					newWorld[row].append(0)
				elif neighborLife in OneToOne:
					newWorld[row].append(1)
					points[g].append(rs.AddPoint(col,row,g))
			
			#current cell is dead...        
			else :  
				#transitions
				if neighborLife in ZeroToZero:
					newWorld[row].append(0)
				elif neighborLife in ZeroToOne:
					newWorld[row].append(1)
					points[g].append(rs.AddPoint(col,row,g))
	#update world
	world = newWorld
	#reset for next gen construction
	newWorld = []

#python list to gh tree
points = th.list_to_tree(points)    

#output points
a = points