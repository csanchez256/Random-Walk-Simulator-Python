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

#a = np.zeros((8,8,3))
#a += 0.5 # "Black" color. Can also be a sequence of r,g,b with values 0-1.
#a[::2, ::2] = 1 # "White" color
#a[1::2, 1::2] = 1 # "White" color


#print a.shape


		

plt.imshow(a, cmap = 'hot'	)


# function that starts walk
def randomWalk(i,j):
	counter = 0
	for itr in range (50):
		x = random.randint(0, 8)
		
		if (x == 0):
			i = i-1
			j = j-1
			counter = counter + 1
			if( (i < 0) or (j < 0) or (i > length) or (j > length) ):
				print "fall"
				break
			else:
		        	a[i][j] = 1	

		elif (x == 1):
			i = i - 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall"
				break
			else:
				a[i][j] = 1

		elif (x == 2):
			i = i - 1
			j = j + 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall"
				break
			else:
				a[i][j] = 1

		elif (x == 3):
			j = j - 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall"
				break
			else:
				a[i][j] = 1
			

		elif (x == 4):
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall"
				break
			else:
				a[i][j] = 1
			
		elif (x == 5):
			j = j + 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall"
				break
			else:
				a[i][j] = 1

		elif (x == 6):
			i = i + 1
			j = j - 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall"
				break
			else:
				a[i][j] = 1

		elif (x == 7):
			i = i + 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall"
				break
			else:
				a[i][j] = 1

		elif (x == 8):
			i = i + 1
			j = j + 1
			counter = counter + 1
			if( i < 0 or j < 0 or i > length or j > length ):
				print "fall"
				break
			else:
				a[i][j] = 1

	print "number of steps is %d" % counter


def testTrial():
	randomWalk(5,8)	
def simulation():
	for i in range (rows):
		for j in range (columns):
			#print random.randint(0, (rows*columns) -1)
			randomWalk(i,j)
testTrial()
#simulation()

for row in a:
	print row

#this is to shift axis' ticks to line up with squares
ax = plt.gca();
#ax.set_yticks(np.arange(-.5, 10, 1));
#ax.set_yticklabels(np.arange(1, 11, 1));

#eliminates x ticks
ax.set(xticks=[] ,yticks=[])


plt.show()

