#At the moment, this script run kmeans on test data it generates itself. Should be trivial to modify to read external data

from random import uniform
from random import randrange
from matplotlib import pyplot as plt

def generate_test_data(numpoints, numcentroids, graph = 0):
    xs = []
    ys = []
    centroids = []
    for centroid in range(numcentroids):
        centroids.append([randrange(-5, 6), randrange(-5, 6)])
    for point in range (numpoints):
        centroid = centroids[randrange(0,numcentroids)]
        cenx = centroid[0]
        ceny = centroid[1]
        xs.append(cenx + uniform(-2, 2))
        ys.append(ceny + uniform(-2, 2))
    if graph == 1:
        plt.scatter(xs, ys)
        plt.show()

    return centroids, [xs, ys]

