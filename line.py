import vector

class Line():
    
    def __init__(self, normalVector, constant=0):
        self.dim = 2
        self.normalVector = normalVector
        if normalVector.isZero():
            raise ValueError('Cannot create a line without a normal vector.')
        if normalVector.dim != self.dim:
            raise ValueError('Normal vector must be 2D.')

        self.constant = constant
        self.basePoint = self.getBasePoint()

    def getBasePoint(self):
        v = self.normalVector.data
        a = v[0]
        b = v[1]

        if a == 0:
            return vector.Vector([0, self.constant/b], self.normalVector.tolerance)
        else:
            return vector.Vector([self.constant/a, 0], self.normalVector.tolerance)   

    def isParallel(self, other):
        return self.normalVector.isParallel(other.normalVector)

    def __eq__(self, other):
        if other == None or not self.isParallel(other):
            return False
        x = self.basePoint
        y = other.basePoint

        z = x.minus(y)
        return self.normalVector.isParallel(z)

    def intersect(self, other):
        if (self.isParallel(other)):
            if self == other:
                return ("SAME", None)
            return ("NO_INTERSECTION", None)

        # The lines definitely intersect now.
        l1 = self
        l2 = other
        if l1.normalVector.data[0] == 0:
            l1 = other
            l2 = self

        a = l1.normalVector.data[0]
        b = l1.normalVector.data[1]
        c = l2.normalVector.data[0]
        d = l2.normalVector.data[1]
        k1 = l1.constant
        k2 = l2.constant

        x = (d*k1 - b*k2)/(a*d - b*c)
        y = (-c*k1 + a*k2)/(a*d - b*c)

        tolerance = max(l1.normalVector.tolerance, l2.normalVector.tolerance)

        return ("INTERSECTION", vector.Vector([x, y], tolerance))

class Line3(Line):

    def __init__(self, basePoint, directionVector):
        self.dim = 3
        self.directionVector = directionVector
        if directionVector.isZero():
            raise ValueError('Cannot create a 3D line without a direction vector.')
        if directionVector.dim != self.dim:
            raise ValueError('Direction vector must be 3D.')

        self.basePoint = basePoint
        if basePoint.dim != self.dim:
            raise ValueError('Base point must be in 3D.')

    def isParallel(self, other):
        return self.directionVector.isParallel(other.directionVector)

    def __eq__(self, other):
        if other == None or not self.isParallel(other):
            return False
        x = self.basePoint
        y = other.basePoint

        z = x.minus(y)
        return self.directionVector.isParallel(z)
                
    def intersect(self, other):
        raise ValueError('Not implemented yet.')
