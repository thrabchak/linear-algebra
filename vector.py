import math
import copy

EPSILON = 0.001

class Vector():

    def __init__(self, data, tolerance=EPSILON):
        self.data = tuple(data)
        self.dim = len(data)
        self.tolerance = tolerance

    def __str__(self):
        return 'Vector: {}'.format(self.data)

    def __eq__(self, other):
        if self.dim != other.dim:
            return False

        for x,y in zip(self.data, other.data):
            if abs(x-y) > self.tolerance:
                return False

        return True

    def plus(self, other):
        result = [x+y for x,y in zip(self.data, other.data)]
        return Vector(result)

    def minus(self, other):
        result = [x-y for x,y in zip(self.data, other.data)]
        return Vector(result)

    def scale(self, value):
        result = [value*x for x in self.data]
        self.data = result

    def dotProduct(self, other):
        product = 0
        for x,y in zip(self.data, other.data):
            product += (x*y)
        return product

    def magnitude(self):
        return math.sqrt(self.dotProduct(self))

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            self.scale(1./mag)

    def angleBetween(self, other, inRadians=True):
        # a dot b = |a| |b| cos theta
        bottom = self.magnitude() * other.magnitude()
        if bottom != 0:
            top = self.dotProduct(other)
            rads = math.acos(top/bottom)
            if inRadians:
                return rads
            else:
                return math.degrees(rads)
        else:
            raise ZeroDivisionError

    def isZero(self):
        return self.magnitude() < self.tolerance

    def isParallel(self, other):
        if self.isZero() or other.isZero():
            return True
        scaleFactor = other.data[0]/self.data[0]
        for x,y in zip(self.data, other.data):
            if x == 0 or y == 0:
                continue
            testScaleFactor = y/x
            if (abs(testScaleFactor-scaleFactor) > self.tolerance):
                return False
        return True

    def isPerpendicular(self, other):
        return abs(self.dotProduct(other)) < self.tolerance

    def project(self, v):
        b = copy.deepcopy(self)
        b.normalize()
        mag = b.dotProduct(v)
        b.scale(mag)
        return b

    def crossProduct(self, other):
        if self.dim == 2:
            a = Vector(self.data.append(0))
            b = Vector(other.data.append(0))
            return a.crossProduct(b)
        elif self.dim == 3:
            a = self.data
            b = other.data
            v = Vector([a[1]*b[2] - a[2]*b[1],
                        a[2]*b[0] - a[0]*b[2],
                        a[0]*b[1] - a[1]*b[0]])
            return v
        else:
            print('Cross product not supported in dimension: ' + str(self.dim))
