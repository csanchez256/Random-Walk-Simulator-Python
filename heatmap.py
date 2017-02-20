import matplotlib.pyplot as plt
import numpy as np
import random

#======================
# This will calculate the expected number of steps
# to fall off
#
#======================

#a = np.random.random((16, 16))

rows = 10
columns = 10
length = rows - 1

#a = np.zeros((10,10))
a = np.arange(100).reshape(rows,columns)

expectedNumTable = np.arange(100).reshape(rows,columns) 

#a = np.zeros((8,8,3))
#a += 0.5 # "Black" color. Can also be a sequence of r,g,b with values 0-1.
#a[::2, ::2] = 1 # "White" color
#a[1::2, 1::2] = 1 # "White" color


#print a.shape

# Uncomment this to see the path of each random walk
#plt.imshow(a, cmap = 'hot',interpolation='nearest')
plt.imshow(expectedNumTable, cmap = 'hot',interpolation='nearest')


# function that starts walk
def randomWalk(i,j):
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


def testTrial():
	print 'index %d\n' % a[5][5]
	expectedNumTable[5][5] = randomWalk(5,5)
	for row in expectedNumTable:
		print row
	
def simulation():
	for i in range (rows):
		for j in range (columns):
			n = randomWalk(i,j)
			print 'index: %d, number of steps: %d\n' % (expectedNumTable[i][j] , n)
			expectedNumTable[i][j] = n

	for row in expectedNumTable:
		print row
#testTrial()
simulation()



#this is to shift axis' ticks to line up with squares
ax = plt.gca();
ax.set_yticks(np.arange(-.5, 10, 1));
ax.set_yticklabels(np.arange(1, 11, 1));

#eliminates x ticks
ax.set(xticks=[] )


plt.show()

