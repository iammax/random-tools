#Reads the number of states, transition matrix, initial populations, and number of timesteps from input.txt, then evolves the system over time for the set number of timesteps

import numpy as np

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
			linecounter += 1
		line = lines[linecounter]
		for i in range (numstates):
			num = float(line.split()[i])
			population[i] = num
		steps = int(lines[linecounter+2])
		return population, matrix, steps, numstates

def largest_change(l1, l2):
	change = 0	
	for i in range(len(l1)):
		delta = abs(l1[i]-l2[i])
		if delta > change:
			change = delta
	return change

population, matrix, steps, numstates = input_reader()
print 'Starting state: \n', population
print 'Transition rates: \n', matrix
step = 0
print 'Populations | largest delta'
print population
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
	population = newpop
	step += 1
