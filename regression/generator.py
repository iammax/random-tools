import random
import numpy as np

def generate_linear(numpoints, random_factor=.5):  #generates random 2-d data that should roughly fit a linear trendline
    m = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    line = lambda x: m*x + b + random_factor*random.uniform(-1, 1)
    arr = np.zeros([numpoints, 2])
    for x in range (numpoints):
        arr[x][0] = random.uniform(-1, 1)
        arr[x][1] = line(arr[x][0])
    np.save('linear_data.npy', arr)
    return arr
