import numpy as np
import matplotlib.pyplot as plt

def randomWalk(N=10000, d=2):
    return np.cumsum(np.random.uniform(-0.5,0.5,(N,d)))

def randomCrossing(timeSeries):
    crossingSeries = np.zeros(timeSeries.shape[0])
    for x in xrange(1,timeSeries.shape[0]):
        if timeSeries[x] > 0 and timeSeries[x-1] < 0:
            crossingSeries[x] = 1
        if timeSeries[x] < 0 and timeSeries[x-1] > 0:
            crossingSeries[x] = 1
    return crossingSeries

def plotRandomWalkXT(N=100000):
    X = randomWalk(N,1)
    plt.plot(X)
    plt.show()

def plotCrossingXT(N=100000):
    X = randomWalk(N,1)
    crossings = randomCrossing(X)
    plt.plot(crossings)
    plt.show()

if __name__ == "__main__":
    plotCrossingXT()
