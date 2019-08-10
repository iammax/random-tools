#This script calculates a linear trendline on whatever data set is fed to it by the command line. If you put "generate" in the command line instead and (optionally) a number of points and randomness, it'll make new data and use that

from random import uniform
import numpy as np
from matplotlib import pyplot as plt
import sys
import loader
import generator

def mean(col):
    return sum(col)/len(col)

def stdev(col, mean):
    total = 0
    for point in col:   
        total += (point-mean)**2
    return np.sqrt(total/len(col))

if sys.argv[1] == 'generate':
    try:
        numpoints = int(sys.argv[2])
        try:
            random_factor = float(sys.argv[3])
            data = generator.generate_linear(numpoints, random_factor)
            print 'Generating data using {0} points at randomness = {1}'.format(numpoints, random_factor)
        except:
            data = generator.generate_linear(numpoints)
            print 'Generating data using {0} points and default randomness'.format(numpoints)
    except:
        data = generator.generate_linear(100)
        print 'Generating data using default number of points and randomness'
else:
    try:
        data = loader.load(sys.argv[1])
    except:
        print 'Please provide the name of the data file in the command line'

xs = data[:,0]
ys = data[:,1]
numpoints = len(xs)
xbar = mean(xs)
ybar = mean(ys)
x_stdev = stdev(xs, xbar)
y_stdev = stdev(ys, ybar)
b1_num = 0
b1_den = 0
r2 = 0


for n in range(numpoints):
    x_diff = xs[n] - xbar
    y_diff = ys[n] - ybar
    b1_num += x_diff*y_diff
    b1_den += x_diff**2
    r2 += x_diff*y_diff
r2 *= (1./numpoints)/(x_stdev*y_stdev)
r2 *= r2
b1 = b1_num/b1_den
b0 = ybar - b1*xbar


pred_xs = np.linspace(-1, 1, numpoints*50)
pred_ys = b1*pred_xs + b0

plt.scatter(data[:,0],data[:,1])
plt.plot(pred_xs, pred_ys, color='red')
plt.title('Trend line: y = {0}x + {1}, r2 = {2}\nx mean: {3} x stdev: {4}\ny mean: {5} y stdev: {6}'.format(b1, b0, r2, xbar, x_stdev, ybar, y_stdev))
plt.show()
