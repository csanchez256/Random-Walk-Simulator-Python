import matplotlib.pyplot as plt
import numpy as np
import random

#======================
# Christopher Sanchez 
# CS 362 Spring 2017 
# Homework 2
#======================

#a = np.random.random((16, 16))

rows = 10
columns = 10
length = rows - 1

# Matrices
a = np.arange(100).reshape(rows,columns)

expectedNumTable = np.arange(100).reshape(rows,columns) 

bonusMatrix = np.arange(64).reshape(8,8)

#a = np.zeros((8,8,3))
#a += 0.5 # "Black" color. Can also be a sequence of r,g,b with values 0-1.
#a[::2, ::2] = 1 # "White" color
#a[1::2, 1::2] = 1 # "White" color


#print a.shape

# Uncomment this to see the path of each random walk
#plt.imshow(a, cmap = 'hot',interpolation='nearest')

#plt.imshow(expectedNumTable, cmap = 'hot',interpolation='nearest')


plt.imshow(bonusMatrix, cmap = 'hot' ,interpolation='nearest')


# function that starts walk
def randomWalk(i,j):
	#a = np.arange(100).reshape(rows,columns)
	counter = 0
	stepsize = 50

	for itr in range (stepsize):
		x = random.randint(0, 8)
		
		if (x == 0):
			i = i-1
			j = j-1
			counter = counter + 1
			if( (i < 0) or (j < 0) or (i > length) or (j > length) ):
				print "fall!\n"
				break
			else:
		        	a[i][j] = 1	

		elif (x == 1):
			i = i - 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall!\n"
				break
			else:
				a[i][j] = 1

		elif (x == 2):
			i = i - 1
			j = j + 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall!\n"
				break
			else:
				a[i][j] = 1

		elif (x == 3):
			j = j - 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall!\n"
				break
			else:
				a[i][j] = 1
			

		elif (x == 4):
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall!\n"
				break
			else:
				a[i][j] = 1
			
		elif (x == 5):
			j = j + 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall!\n"
				break
			else:
				a[i][j] = 1

		elif (x == 6):
			i = i + 1
			j = j - 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall!\n"
				break
			else:
				a[i][j] = 1

		elif (x == 7):
			i = i + 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall!\n"
				break
			else:
				a[i][j] = 1

		elif (x == 8):
			i = i + 1
			j = j + 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall!\n"
				break
			else:
				a[i][j] = 1

	#print "number of steps is %d\n" % counter
	return counter




#=========================== NORTH EDGE =========================================================

# function that starts walk
def NorthEdge(i,j):
	#a = np.arange(100).reshape(rows,columns)
	counter = 0
	stepsize = 50

	for itr in range (stepsize):
		x = random.randint(0, 8)
		
		if (x == 0):
			i = i-1
			j = j-1
			counter = counter + 1
			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1

		elif (x == 1):
			i = i - 1
			counter = counter + 1

			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1

		elif (x == 2):
			i = i - 1
			j = j + 1
			counter = counter + 1

			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1

		elif (x == 3):
			j = j - 1
			counter = counter + 1

			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1
			

		elif (x == 4):
			counter = counter + 1

			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1
			
		elif (x == 5):
			j = j + 1
			counter = counter + 1

			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1

		elif (x == 6):
			i = i + 1
			j = j - 1
			counter = counter + 1

			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1

		elif (x == 7):
			i = i + 1
			counter = counter + 1

			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1

		elif (x == 8):
			i = i + 1
			j = j + 1
			counter = counter + 1

			if(i < 0):
				print "fall"
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1

	#print "number of steps is %d\n" % counter
	return counter



#====================================================================================


def bonusWalk(i,j):
	#a = np.arange(100).reshape(rows,columns)
	counter = 0
	stepsize = 500

	for itr in range (stepsize):
		x = random.randint(0, 8)
		
		if (x == 0):
			i = i-1
			j = j-1
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break
				

		elif (x == 1):
			i = i - 1
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break

		elif (x == 2):
			i = i - 1
			j = j + 1
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break

		elif (x == 3):
			j = j - 1
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break
			

		elif (x == 4):
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break
			
		elif (x == 5):
			j = j + 1
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break

		elif (x == 6):
			i = i + 1
			j = j - 1
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break

		elif (x == 7):
			i = i + 1
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break

		elif (x == 8):
			i = i + 1
			j = j + 1
			counter = counter + 1
			if (i < 0):
				i = i+1
			if(j < 0):
				j = j+1
			if (i > 7):
				i = i-1 
			if (j > 7):
				j = j-1
		        
			bonusMatrix[i][j] = 1
			break

	#print "number of steps is %d\n" % counter
	#return counter



# Just a test function for hard coded values
def bonus():
	print 'index of bonus matrix %d\n' % bonusMatrix[2][4]
	#bonusMatrix[2][4] = bonusWalk(2,4)

	trials = 500
	for itr in range (trials):
		bonusWalk(2,4)

	for row in bonusMatrix:
		print row




# This function is the driver. It iterates every index in the board.	
def simulation():
	for i in range (rows):
		for j in range (columns):

			average = runMultipleSimulations(i,j)
			
			print 'index: %d, number of steps: %d\n' % (expectedNumTable[i][j] , average)

			expectedNumTable[i][j] = average

	for row in expectedNumTable:
		print row



# this function will run several times for each index to get an average
# The value of numTrials determines how many times each index is tested
def runMultipleSimulations(i, j):

	averages = []
	numTrials = 100

	print "i and j: %s %s" % (i,j)

	for itr in range(numTrials):

		a = randomWalk(i,j) 

		#a = NorthEdge(i,j)
			
		averages.append(a) #store all the expected values in an array, then compute the average
	
	average = ( sum( int (n) for n in averages ) ) / numTrials

	print "average is %s" % average

	return average

#==========================================================================================


#testTrial()
#simulation()

bonus()

#this is to shift axis' ticks to line up with squares
ax = plt.gca();
#ax.set_yticks(np.arange(-.5, 10, 1));
#ax.set_yticklabels(np.arange(1, 11, 1));

#eliminates x ticks
ax.set(xticks=[] )

plt.show()

