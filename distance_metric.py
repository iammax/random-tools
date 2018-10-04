#Calculates the lN norm of two provided vectors, entered in text files.
#call this script from command: "python l_norm.py vector_1.txt vector_2.txt N"

import sys
import numpy as np
v1 = np.genfromtxt(sys.argv[1])
v2 = np.genfromtxt(sys.argv[2])

def l0(v1, v2): #differences
	dim = len(v1)
	total = 0
	for q in range(dim):
		if v1[q] !=v2[q]:
			total += 1
	return total

def l1(v1, v2): #manhattan
	dim = len(v1)
	total = 0
	for q in range (dim):
		total += abs(v2[q]-v1[q])
	return total

def l2(v1, v2): #euclidian distance
	dim = len(v1)
	total = 0
	for q in range (dim):
		total += (v2[q]-v1[q])**2
	return np.sqrt(total)

def linf(v1, v2): #chebyshev
	dim = len(v1)
	highest = 0
	for q in range(dim):
		diff = abs(v2[q]-v1[q])
		if diff > highest:
			highest = diff
	return highest	

if len(v1) != len(v2):
	print "Your vectors are of different lengths: {0} for {1}, {2} for {3}".format(len(v1), sys.argv[1], len(v2), sys.argv[2])
	quit()
print "Vector 1:\n {0}".format(v1)
print "Vector 2:\n {0}".format(v2)

print """\nEnter the number of the distance metric you want between the two vectors:\n
0: All of the below
1: l0 norm (number of differences)
2: Manhattan distance (l1 norm)
3: Euclidian distance (l2 norm)
4: Chebyshev distance (l-inf norm)"""

selection = input('Selection: ')
if selection == 0:
	print "Number of differences/L0 norm: ", l0(v1, v2)
	print 'Manhattan distance/L1 norm: ', l1(v1, v2)
	print 'Euclidian distance/L2 norm: ', l2(v1, v2)
	print 'Chebyshev distance/Linf norm: ', linf(v1, v2)
elif selection == 1:
	print "Result: ", l0(v1, v2)
elif selection == 2:
	print "Result: ", l1(v1, v2)
elif selection == 3:
	print "Result: ", l2(v1, v2)
elif selection == 4:
	print "Result: ", linf(v1, v2)
else:
	print "That isn't an option"
