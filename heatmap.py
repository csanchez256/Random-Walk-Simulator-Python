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
def NorthEdge(i,j,numTrials):
	#a = np.arange(100).reshape(rows,columns)

	start_i = i
	start_j = j

	counter   = 0
	n_counter = 0
	stepsize  = 50

	for itr in range (stepsize):
		x = random.randint(0, 8)
		
		if (x == 0):
			i = i-1
			j = j-1
			counter = counter + 1
			if(i < 0):
				print "fall"
				n_counter = n_counter + 1
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
				n_counter = n_counter + 1
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
				n_counter = n_counter + 1
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
				n_counter = n_counter + 1
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1
			

		elif (x == 4):
			counter = counter + 1

			if(i < 0):
				print "fall"
				n_counter = n_counter + 1
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
				n_counter = n_counter + 1
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
				n_counter = n_counter + 1
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
				n_counter = n_counter + 1
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
				n_counter = n_counter + 1
				break;

			elif ( (j < 0) or (i > length) or (j > length) ):
				print "fell"

			else:
		        	a[i][j] = 1

	#print "number of steps is %d\n" % counter
	#returns a tuple

	return counter, n_counter



#====================================================================================

#def probability(i,j,numTrials):



#====================================================================================

def bonusWalk(i,j):
	#a = np.arange(100).reshape(rows,columns)
	counter = 0
	stepsize = 5000
	stop = False

	for itr in range (stepsize):
		x = random.randint(0, 8)
		
		if (x == 0):
			i = i-1
			j = j-1
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break

		elif (x == 1):
			i = i - 1
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break
			

		elif (x == 2):
			i = i - 1
			j = j + 1
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break
			

		elif (x == 3):
			j = j - 1
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break
			

		elif (x == 4):
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break
			
			
		elif (x == 5):
			j = j + 1
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break
			

		elif (x == 6):
			i = i + 1
			j = j - 1
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break
			

		elif (x == 7):
			i = i + 1
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break
			

		elif (x == 8):
			i = i + 1
			j = j + 1
			counter = counter + 1
			if (i < 0):
				i = i+1
				stop = True
			if(j < 0):
				j = j+1
				stop = True
			if (i > 7):
				i = i-1 
				stop = True
			if (j > 7):
				j = j-1
				stop = True
		        
			if (stop == True): 
				bonusMatrix[i][j] = counter
				break
			

# Just a test function for hard coded values
def bonus():
	print 'index of bonus matrix %d\n' % bonusMatrix[2][4]
	#bonusMatrix[2][4] = bonusWalk(2,4)

	trials = 500000
	for itr in range (trials):
		bonusWalk(2,4)

	for row in bonusMatrix:
		print row


# This function is the driver. It iterates every index in the board.	
def simulation():
	for i in range (rows):
		for j in range (columns):

			average = runMultipleSimulations(i,j)
			
			#print 'index: %d, number of steps: %d\n' % (expectedNumTable[i][j] , average)

			expectedNumTable[i][j] = average[0]
			probabilityTable[i][j] = average[1] 

	for row in expectedNumTable:
		print row


# this function will run several times for each index to get an average
# The value of numTrials determines how many times each index is tested
def runMultipleSimulations(i, j):

	averages = []
	probabilities = []
 	numTrials = 500

	print "i and j: %s %s" % (i,j)

	for itr in range(numTrials):

		b = randomWalk(i,j) 

		a = NorthEdge(i,j,numTrials)
			
		averages.append(b) #store all the expected values in an array, then compute the average
		probabilities.append(a[1])

	 
	average = ( sum( int (n) for n in averages ) ) / numTrials
	prob = (sum (float (n) for n in probabilities )) 

	print 'probabilites is %d' % prob

	print "average is %s" % average

	return average, prob

#==========================================================================================


#testTrial()
simulation()

#bonus()

#this is to shift axis' ticks to line up with squares
ax = plt.gca();
#ax.set_yticks(np.arange(-.5, 10, 1));
#ax.set_yticklabels(np.arange(1, 11, 1));

#eliminates x ticks
ax.set(xticks=[] )

plt.show()

