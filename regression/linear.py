#This script generates some random 2d data and then calculates the linear regression line + r squared. 

#Tweakables: numpoints = number of points. Random_factor = how much randomness should be in the data. If it's 0, the points will end up exactly on the regression line. Something between .1 and .5 usually makes somewhat coherent data.
numpoints = 100
random_factor = .5

from random import uniform
import numpy as np
from matplotlib import pyplot as plt

def generate(m, b, xs, random_factor, ys=1): 
    ys += 1
    line = lambda x: m*x + b + random_factor*uniform(-1, 1)
    arr = np.zeros([xs, ys])
    for x in range (xs):
        arr[x][0] = uniform(-1, 1)
        arr[x][1] = line(arr[x][0])
    return arr

def mean(col):
    return sum(col)/len(col)

def stdev(col, mean):
    total = 0
    for point in col:   
        total += (point-mean)**2
    return np.sqrt(total/len(col))

m = uniform(-1, 1)
b = uniform(-1, 1)
data = generate(m, b, numpoints, random_factor)
xs = data[:,0]
ys = data[:,1]
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
