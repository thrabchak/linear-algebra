import vector
import line

class Plane():
    
    def __init__(self, normalVector, constant=0):
        self.dim = 3
        self.normalVector = normalVector
        if normalVector.isZero():
            raise ValueError('Cannot create a plane without a normal vector.')
        if normalVector.dim != self.dim:
            raise ValueError('Normal vector must be 3D.')

        self.constant = constant
        self.basePoint = self.getBasePoint()

    def getBasePoint(self):
        v = self.normalVector.data
        a = v[0]
        b = v[1]
        c = v[2]

        if a == 0:
            return vector.Vector([0, 0, self.constant/c], self.normalVector.tolerance)
        else:
            return vector.Vector([self.constant/a, 0, 0], self.normalVector.tolerance)   

    def isParallel(self, other):
        return self.normalVector.isParallel(other.normalVector)

    def __eq__(self, other):
        if other == None or not self.isParallel(other):
            return False
        x = self.basePoint
        y = other.basePoint
        z = x.minus(y)
        return self.normalVector.isParallel(z)

    def intersectWithLine(self, l):
        if not isinstance(l, line.Line3):
            raise ValueError('Argument is not a line.')

        if (self.normalVector.isPerpendicular(l.directionVector)):
            x = self.basePoint
            y = l.basePoint
            z = x.minus(y)
            if self.normalVector.isPerpendicular(z):
                return ("SAME", None)
            return ("NO_INTERSECTION", None)

        n = self.normalVector
        u = l.directionVector
        w = l.basePoint.minus(self.basePoint)
        s = (-1*n.dotProduct(w)) / (n.dotProduct(u))

        p = l.directionVector.getCopy()
        pt = l.basePoint.plus(p.scale(s))
        return ("INTERSECTION", pt)
