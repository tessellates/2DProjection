# What is a plane?
# (p — p_0) . n = 0
# The plane is all points p that satisfy the equation
# p_0 is any point on the plane, n is the "normal vector" of the plane. It is orthogonal with the plane.
# Note that p - p_0 is a vector that has to be orthogonal to n for the equation to be satisfied.

# For example take a 3D space defined by 3 unit vectors orthogonal to each other named x, y, z respectively.
# The plane spanned by 
import math

class Coordinate():
    def __init__(self, x, y, z):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def z(self):
        return self._z

    def __add__(self, other):  
        return Coordinate(self._x + other.x, self._y + other.y, self._z + other.z)
    
    def __sub__(self, other):  
        return self + -1*other

    def __truediv__(self, other):  
        return self._x / other.x + self._y  / other.y + self._z  / other.z

    def __floordiv__(self, other):  
        return self._x / other.x + self._y  / other.y + self._z  / other.z

    def __mul__(self, other):  
        return self._x * other.x + self._y * other.y + self._z * other.z

    def __radd__(self, scalar):  
        return Coordinate(self._x + scalar, self._y + scalar, self._z + scalar)

    def __rmul__(self, scalar):  
        return Coordinate(self._x * scalar, self._y * scalar, self._z * scalar)

    def __rtruediv__(self, scalar):  
        return Coordinate(self._x / scalar, self._y / scalar, self._z / scalar)

    def __rfloordiv__(self, scalar):  
        return Coordinate(self._x / scalar, self._y / scalar, self._z / scalar)

    def __str__(self):
        return 'C:({},{},{})'.format(self.x, self.y, self.z)

    def normalizedVector(point):
        d = math.sqrt(point.x**2 + point.y**2 + point.z**2)
        p = (1/d) * point
        return p

    def TD(x, y):
        return Coordinate(x,y,0)
class Line():
    def __init__(self, point, direction):
        self._point = point
        self._direction = direction
        

    @property
    def direction(self):
        return self._direction

    @property
    def point(self):
        return self._point

    def pointOnLine(self, t):
        return t * self._direction + self._point

    def createLine(p1, p2):
        return Line(p1, Coordinate.normalizedVector(p1-p2))

class Plane():
    def __init__(self, point, normal):
        self._point = point
        self._normal = normal

    def intersection(self, line):
        t = (self._point - line.point) * (self._normal) / (line.direction * (self._normal))
        return line.pointOnLine(t)

c = Coordinate(1,1,1)
w = Plane( c, Coordinate.normalizedVector(c) )
l = Line( Coordinate(0,0,0), Coordinate.normalizedVector(c) )
print(w.intersection(l))