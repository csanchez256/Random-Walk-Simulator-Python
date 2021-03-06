#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import random

#====================================================================================
# Christopher Sanchez 
# CS 362 Spring 2017 
# Homework 2
# NOTE: MAKE SURE YOU INSTALL MATPLOTLIB LIBRARIES
# COMMAND: python -m pip install -U matplotlib
# SOURCE: https://matplotlib.org/users/installing.html#installing-an-official-release
#
#====================================================================================

#this is a test

#a = np.random.random((16, 16))

rows = 10
columns = 10
length = rows - 1

# Matrices
a = np.arange(100).reshape(rows,columns)

expectedNumTable = np.arange(100).reshape(rows,columns) 

bonusMatrix = np.arange(64).reshape(8,8)

probabilityTable = np.arange(100).reshape(rows,columns)

#print a.shape

# Uncomment this to see the path of each random walk
#plt.imshow(a, cmap = 'hot',interpolation='nearest')

#plt.imshow(expectedNumTable, cmap = 'hot',interpolation='nearest')


#======================
# Set first argument to 
# whatever matrix you
# WANT TO DISPLAY
#======================

plt.imshow(expectedNumTable, cmap = 'hot' ,interpolation='nearest')

# function that prints a falling off the grid
def checkFall(i, j):
	if( (i < 0) or (j < 0) or (i > length) or (j > length) ):
				print ("fall!\n")
				return True


# function that starts walk
def randomWalk(i,j):

	counter = 0
	stepsize = 50

	for itr in range (stepsize):
		x = random.randint(0, 8)
		
		if (x == 0):
			i = i-1
			j = j-1
			counter += 1
			if( checkFall(i,j) ):
				break
	

		elif (x == 1):
			i = i - 1
			counter += 1
			if( checkFall(i,j) ):
				break


		elif (x == 2):
			i = i - 1
			j = j + 1
			counter += 1
			if( checkFall(i,j) ):
				break


		elif (x == 3):
			j = j - 1
			counter += 1
			if( checkFall(i,j) ):
				break
		

		elif (x == 4):
			counter += 1
			if( checkFall(i,j) ):
				break

			
		elif (x == 5):
			j = j + 1
			counter += 1
			if( checkFall(i,j) ):
				break


		elif (x == 6):
			i = i + 1
			j = j - 1
			counter += 1
			if( checkFall(i,j) ):
				break


		elif (x == 7):
			i = i + 1
			counter += 1
			if( checkFall(i,j) ):
				break


		elif (x == 8):
			i = i + 1
			j = j + 1
			counter += 1
			if( checkFall(i,j) ):
				break


	#print "number of steps is %d\n" % counter
	return counter




#=========================== NORTH EDGE =========================================================

# function that starts walk
def NorthEdge(i,j,numTrials):

	counter   = 0
	n_counter = 0
	stepsize  = 50

	for itr in range (stepsize):
		x = random.randint(0, 8)
		
		if (x == 0):
			i = i-1
			j = j-1
			counter += 1
			if(checkFall(i,j)):
				n_counter += 1
				break;


		elif (x == 1):
			i = i - 1
			counter += 1

			if(checkFall(i,j)):
				n_counter += 1
				break;


		elif (x == 2):
			i = i - 1
			j = j + 1
			counter += 1

			if(checkFall(i,j)):
				n_counter += 1
				break;


		elif (x == 3):
			j = j - 1
			counter += 1

			if(checkFall(i,j)):
				n_counter += 1
				break;
			

		elif (x == 4):
			counter += 1

			if(checkFall(i,j)):
				n_counter += 1
				break;

			
		elif (x == 5):
			j = j + 1
			counter += 1

			if(checkFall(i,j)):
				n_counter += 1
				break;


		elif (x == 6):
			i = i + 1
			j = j - 1
			counter += 1

			if(checkFall(i,j)):
				n_counter += 1
				break;


		elif (x == 7):
			i = i + 1
			counter += 1

			if(checkFall(i,j)):
				n_counter += 1
				break;


		elif (x == 8):
			i = i + 1
			j = j + 1
			counter += 1

			if(checkFall(i,j)):
				n_counter += 1
				break;


	#print "number of steps is %d\n" % counter

	#returns a tuple
	return counter, n_counter



# This function is the driver. It iterates every index in the board.	
def simulation():
	for i in range (rows):
		for j in range (columns):

			average = runMultipleSimulations(i,j)
			
			#print 'index: %d, number of steps: %d\n' % (expectedNumTable[i][j] , average)

			expectedNumTable[i][j] = average[0]
			probabilityTable[i][j] = average[1] 

	for row in expectedNumTable:
		print (row)


# this function will run several times for each index to get an average
# The value of numTrials determines how many times each index is tested
def runMultipleSimulations(i, j):

	averages = []
	probabilities = []
	numTrials = 50

	print ("i and j: %s %s" % (i,j))

	for itr in range(numTrials):

		b = randomWalk(i,j) 

		ne_counter = NorthEdge(i,j,numTrials)
			
		averages.append(b) #store all the expected values in an array, then compute the average
		probabilities.append(ne_counter[1])

	 
	average = ( sum( int (n) for n in averages ) ) / numTrials
	prob = (sum (float (n) for n in probabilities )) 

	print ('probabilites is %d' % prob)

	print ("average is %s" % average)

	return average, prob

#==========================================================================================


simulation()


#this is to shift axis' ticks to line up with squares
ax = plt.gca();
ax.set(xticks=[] )

plt.show()

