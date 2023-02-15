
import matplotlib.pyplot as plt
from plane import *
from space import *
import matplotlib.patches as patches
from PIL import Image


def CreateProjection( ):


    # Create figure and axes
    fig, ax = plt.subplots()
    fig.set_size_inches(10.5,10.5)


    def plotCoordinate(a, b):
        x_values = [a.x, b.x]
        y_values = [a.y, b.y]
        plt.plot(x_values, y_values, marker = 'o')

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    x = 8
    cpv = list()
    for i in range(x):
        for j in range(x):
            cpv += CreateLines(Coordinate(0,0+j*2,0+i*2), 2)
            cpv += CreateLines(Coordinate(8,0+j*2,0+i*2), 2)
            if (i == 5):
                for l in range(1,x-1):
                    cpv += CreateLines(Coordinate(l*2,0+j*2,0+i*2), 2)

        for pair in cpv:
            plotCoordinate(pair[0], pair[1])


    plt.show()

CreateProjection()