import math
import copy

EPSILON = 0.001

class Vector():

    def __init__(self, data, tolerance=EPSILON):
        self.data = tuple(data)
        self.dim = len(data)
        self.tolerance = tolerance
        if 1 <= tolerance <= 0:
            raise ValueError('Tolerance must be between 0 and 1.')

    def __str__(self):
        digits = 0
        decimal = self.tolerance % 1
        while(decimal < 1):
            decimal *= 10
            digits += 1

        v = ['<']
        for i in self.data:
            v.append('{}'.format(round(i, digits)))
            v.append(', ')
        v.pop()
        v.append('>')
        return ''.join(v)

    def __eq__(self, other):
        if other == None:
            return False

        if self.dim != other.dim:
            raise ValueError('Vectors have different dimensions.')

        for x,y in zip(self.data, other.data):
            if abs(x-y) > self.tolerance:
                return False

        return True

    def plus(self, other):
        if self.dim != other.dim:
            raise ValueError('Vectors have different dimensions.')

        result = [x+y for x,y in zip(self.data, other.data)]
        return Vector(result)

    def minus(self, other):
        if self.dim != other.dim:
            raise ValueError('Vectors have different dimensions.')

        result = [x-y for x,y in zip(self.data, other.data)]
        return Vector(result)

    def scale(self, value):
        result = [value*x for x in self.data]
        self.data = result
        return self

    def dotProduct(self, other):
        if self.dim != other.dim:
            raise ValueError('Vectors have different dimensions.')

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
        return self

    def angleBetween(self, other, inRadians=True):
        if self.dim != other.dim:
            raise ValueError('Vectors have different dimensions.')

        # a dot b = |a| |b| cos theta
        bottom = self.magnitude() * other.magnitude()
        if bottom != 0:
            top = self.dotProduct(other)
            lhs = top/bottom

            # Have to account for floating point error propagation here.
            if (abs(lhs-1) < self.tolerance):
                lhs = 1
            elif (abs(lhs+1) < self.tolerance):
                lhs = -1

            rads = math.acos(lhs)
            if inRadians:
                return rads
            else:
                return math.degrees(rads)
        else:
            raise ZeroDivisionError

    def isZero(self):
        return self.magnitude() < self.tolerance

    def isParallel(self, other):
        if self.dim != other.dim:
            raise ValueError('Vectors have different dimensions.')

        if self.isZero() or other.isZero():
            return True
        
        angle = self.angleBetween(other)
        if angle < self.tolerance or abs(angle - math.pi) < self.tolerance:
            return True


    def isPerpendicular(self, other):
        if self.dim != other.dim:
            raise ValueError('Vectors have different dimensions.')

        return abs(self.dotProduct(other)) < self.tolerance

    def project(self, v):
        if self.dim != v.dim:
            raise ValueError('Vectors have different dimensions.')

        b = copy.deepcopy(self)
        b.normalize()
        mag = b.dotProduct(v)
        b.scale(mag)
        return b

    def crossProduct(self, other):
        if self.dim != other.dim:
            raise ValueError('Vectors have different dimensions.')

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

    def getCopy(self):
        return copy.deepcopy(self)