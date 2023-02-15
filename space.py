from plane import *

def CreateLines(origin, size):
    viewer = Coordinate(5,5, -1)

    def CreateCube(origin, size):
        p1 = origin
        p2 = origin + Coordinate(size, 0, 0)
        p3 = origin + Coordinate(0, 0, size)
        p4 = origin + Coordinate(0, size, 0)
        p5 = p4 +  Coordinate(size, 0, 0)
        p6 = p4 + Coordinate(0, 0, size)
        p7 = p6 + Coordinate(size, 0, 0)
        p8 = p2 + Coordinate(0, 0, size)
        points = [p1, p2, p3, p4, p5, p6, p7, p8]
        return points

    pp = Plane(Coordinate(0,0,0), Coordinate(0,0,1))

    cube = CreateCube(origin, size)

    projectedPoints = list()
    for point in cube:
        line = Line.createLine(viewer, point)
        projectedPoints.append(pp.intersection(line))

    pairs = list()
    for i in range(len(projectedPoints)):
        for j in range(i+1, len(projectedPoints)):
            pairs.append(tuple((projectedPoints[i], projectedPoints[j])))
    return pairs
