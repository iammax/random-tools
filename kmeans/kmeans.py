#At the moment, this script run kmeans on test data it generates itself. Should be trivial to modify to read external data
#Todo: Re-implement this with faster vectorized method

from random import uniform
from random import randrange
from matplotlib import pyplot as plt
import numpy as np

def generate_test_data(numpoints, numcentroids, graph = 0):

    points = np.array([0,0])
    centroids = []
    for centroid in range(numcentroids):
        centroids.append([randrange(-5, 6), randrange(-5, 6)])
    for point in range (numpoints):
        centroid = centroids[randrange(0,numcentroids)]
        cenx = centroid[0]
        ceny = centroid[1]
        points = np.vstack([points, [cenx + uniform(-2, 2), ceny + uniform(-2, 2)]])
    if graph == 1:
        plt.scatter(xs, ys)
        plt.show()
    
    return centroids, points

def distance(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2


threshold = 1e-5 #if the biggest change in centroid position is smaller than this, we know it's done, and program aborts
numpoints = 1000
k = 3 #number of centroids to use for k-means. Note that this can't be more than the amount of things in colors below
centroids, points = generate_test_data(numpoints, 3) #the 3 here is how many imaginary clusters to generate the data around; it's not really related to k above. 3 seems relatively useful but feel free to change it if desired
colors = ['r', 'g', 'b', 'purple', 'orange', 'yellow']
max_iters = 100
current_iter = 1
centroids = np.array([uniform(-5, 5), uniform(-5, 5)])
for extra_centroid in range(k-1):
    centroids = np.vstack([centroids, [uniform(-5, 5), uniform(-5, 5)]])
#centroids = np.array([[uniform(-5, 5), uniform(-5, 5)],[uniform(-5, 5), uniform(-5, 5)],[uniform(-5, 5), uniform(-5, 5)]]) #the initial randomly assigned centroids
plt.scatter(points[:,0], points[:,1], color = 'black')
plt.scatter(centroids[:,0], centroids[:,1], marker = 'x', s = 100, color = colors)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.ion()
plt.title('Initial random centroids + some mildly clustered random points')
plt.show(block=False)
print ('Initial randomly assigned centroids: \n', centroids)
input("Press Enter to continue... (remember to click here to return focus to the terminal window)")
while current_iter < max_iters:
    owners = {} 
    for owner in range (len(centroids)):
        owners[owner] = [0,0]
    point_colors = []
    for point in points:
        distances = []
        for centroid in centroids:
            distances.append(distance(point, centroid))
        assigned_centroid = distances.index(min(distances))
        owners[assigned_centroid] = np.vstack([owners[assigned_centroid], point])
        point_colors.append(colors[assigned_centroid])
#    print (centroids, '\n')
#    print (points, '\n')
#    for owner in owners:
#        print(owner, owners[owner][1:], '\n')
    plt.clf()
    plt.title('Points and centroids for iteration {0}'.format(current_iter))
    plt.scatter(points[:,0], points[:,1], color = point_colors)
    plt.scatter(centroids[:,0], centroids[:,1], marker = 'x', s = 300, color = colors)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    new_centroids = [0,0]
    centroid_deltas = []
    for centroid_num in range(k):
        owned_points = owners[centroid_num][1:]
        new_x = np.mean(owned_points[:,0])
        new_y = np.mean(owned_points[:,1])
        new_centroids = np.vstack([new_centroids, [new_x, new_y]])
        centroid_deltas.append(distance(centroids[centroid_num], [new_x, new_y]))
    centroids = new_centroids[1:]
    print('New centroids: \n', centroids)
    delta = max(centroid_deltas)
    print('Largest change in centroid position: ', delta)
    if delta < threshold and current_iter > 1: 
        print('K-means converged at above positions! Terminating...')
        current_iter = max_iters + 1
    input('Press Enter to continue...')
    current_iter += 1
