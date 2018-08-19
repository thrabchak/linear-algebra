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
        if not isinstance(other, Plane):
            raise ValueError('Argument is not a plane.')

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

    def intersectWithPlane(self, p):
        if not isinstance(p, Plane):
            raise ValueError('Argument is not a plane.')

        if (self.isParallel(p)):
            if self == p:
                return ("SAME", None)
            return ("NO_INTERSECTION", None)

        n1 = self.normalVector
        n2 = p.normalVector
        u = n1.crossProduct(n2).normalize()

        a = self.normalVector.data[0]
        b = self.normalVector.data[1]
        c = self.normalVector.data[2]
        d = p.normalVector.data[0]
        e = p.normalVector.data[1]
        f = p.normalVector.data[2]
        k1 = self.constant
        k2 = p.constant

        if (u.data[0] != 0):
            x = 0
            y = (b*f - c*k2) / (b*f - c*e)
            z = (b*k2 - b*e) / (b*f - c*e)
        elif (u.data[1] != 0):
            x = (a*f - c*k2) / (a*f - c*d)
            y = 0
            z = (a*k2 - a*d) / (a*f - c*d)
        else:
            x = (a*e - b*k2) / (a*e - b*d)
            y = (a*k2 - a*d) / (a*e - b*d)
            z = 0
        pt = vector.Vector([x,y,z])
        l = line.Line3(pt, u)

        return ("INTERSECTION", l)
