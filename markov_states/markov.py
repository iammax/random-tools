#Reads the number of states, transition matrix, initial populations, and number of timesteps from input.txt, then evolves the system over time for the set number of timesteps

import numpy as np
np.warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import scipy.linalg as la
from random import random

def input_reader():
	with open('input.txt', 'r') as infile:
		lines = infile.readlines()
		numstates = int(lines[1])
		matrix = np.zeros([numstates, numstates])
		population = np.zeros([numstates])
		linecounter = 3
		readmatrix = False
		while readmatrix == False:
			line = lines[linecounter]
			if line == 'Population\n':
				readmatrix = True
			else:
				for i in range (numstates):
					num = float(line.split()[i])
					matrix[linecounter-3][i] = num
				matrix[linecounter-3] = normalize(matrix[linecounter-3])
			linecounter += 1
		line = lines[linecounter]
		for i in range (numstates):
			num = float(line.split()[i])
			population[i] = num
		population = normalize(population)
		steps = int(lines[linecounter+2])
		return population, matrix, steps, numstates

def normalize(vector):
	total = sum(vector)
	outvec = [q*(1/float(total)) for q in vector]
	return outvec

def largest_change(l1, l2):
	change = 0	
	for i in range(len(l1)):
		delta = abs(l1[i]-l2[i])
		if delta > change:
			change = delta
	return change

def onefinder(vals):
	dim = len(vals)
	for q in range (dim):
		if np.isclose(1, vals[q]):
			return q
	print "Couldn't find 1 eigenvalue"

population, matrix, steps, numstates = input_reader()
print 'Starting state: \n', population
print 'Transition rates: \n', matrix
matrix = np.array(matrix)
vals, vecs = np.linalg.eig(matrix.T)
vecs = vecs.T
#print 'evals: ', vals
#print 'evecs: \n', vecs
onelocation = onefinder(vals)
eqvec = np.real(normalize(vecs[onelocation]))
print 'Equilibrium populations: ', eqvec
#for vec in vecs:
#	print 'vec: ', vec, 'normalized: ', normalize(vec), 'vec/sum', vec/vec.sum()
#	print normalize(vec)
step = 0
print 'Populations | largest delta'
print population
results = []
results = population
while step < steps:
#	print "Step {0}...".format(step)
	newpop = np.zeros([numstates])
	for i in range (0, numstates):
		pop_i = population[i]
		transitions = matrix[i]	
		for j in range (0, numstates):
#			print 'i: {0} pop_i: {1} transition: {2} adding: {3}'.format(i, pop_i, transitions[j], pop_i*transitions[j])
			newpop[j] += (pop_i*transitions[j])
	biggest_change = largest_change(population, newpop)
	print newpop, biggest_change
	if biggest_change < 10e-7:
		print 'Equilibirum'
		step = steps
	results = np.vstack([results, newpop])
	population = newpop
	step += 1
dim = len(results.T)
for q in range (dim):
#for item in results.T:
	item = results.T[q]
	plt.plot(range(len(item)), item, label = "State # {0}".format(q))
plt.xlabel('Timestep')
plt.ylabel('Population')
#plt.ylim([0,1])
plt.legend()
print 'Prediction equilibrium populations are close? '
print np.isclose(eqvec, population)
plt.show()
