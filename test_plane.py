import unittest
import plane
import vector
import line

V = vector.Vector
P = plane.Plane
L3 = line.Line3

class TestPaneMethods(unittest.TestCase):

    def test_create(self):
        norm = V([1,2,3])
        p = P(norm, 1)
        self.assertNotEqual(p, None)

    def test_parallel(self):
        n1 = V([1, 1, 2])
        p1 = P(n1, 3)
        n2 = V([2, 2, 4])
        p2 = P(n2, 4)
        self.assertTrue(p1.isParallel(p2))

    def test_not_parallel(self):
        n1 = V([2, 1, 2])
        p1 = P(n1, 3)
        n2 = V([2, 2, 4])
        p2 = P(n2, 4)
        self.assertFalse(p1.isParallel(p2))

    def test_1(self):
        n1 = V([-.412, 3.806, 0.728])
        p1 = P(n1, -3.46)
        n2 = V([1.03, -9.515, -1.82])
        p2 = P(n2, 8.65)
        self.assertTrue(p1.isParallel(p2))
        self.assertEqual(p1, p2)

    def test_2(self):
        n1 = V([2.611, 5.528, 0.283])
        p1 = P(n1, 4.6)
        n2 = V([7.715, 8.306, 5.342])
        p2 = P(n2, 3.76)
        self.assertFalse(p1.isParallel(p2))
        self.assertNotEqual(p1, p2)

    def test_3(self):
        n1 = V([-7.926, 8.625, -7.212])
        p1 = P(n1, -7.952)
        n2 = V([-2.642, 2.875, -2.404])
        p2 = P(n2, 2.443)
        self.assertTrue(p1.isParallel(p2))
        self.assertNotEqual(p1, p2)

    def test_intersect_with_line(self):
        p = P(V([2,1,-4]), 4)
        l = L3(V([0,2,0]), V([1,3,1]))
        (a, b) = p.intersectWithLine(l)
        self.assertEqual(a, "INTERSECTION")
        self.assertEqual(b, V([2,8,2]))

    def test_intersect_with_line2(self):
        p = P(V([2,1,-4]), 4)
        l = L3(V([1,4,0]), V([1,2,1]))
        (a, b) = p.intersectWithLine(l)
        self.assertEqual(a, "NO_INTERSECTION")
        self.assertEqual(b, None)

    def test_intersect_with_line3(self):
        p = P(V([2,1,-4]), 4)
        l = L3(V([0,4,0]), V([1,2,1]))
        (a, b) = p.intersectWithLine(l)
        self.assertEqual(a, "SAME")
        self.assertEqual(b, None)

    def test_intersect_with_plane(self):
        p1 = P(V([1,1,1]), -1)
        p2 = P(V([1,2,3]), -4)
        (a, b) = p1.intersectWithPlane(p2)
        l = L3(V([2,-3,0]), V([1,-2,1]))
        self.assertTrue(b.isParallel(l))

if __name__ == '__main__':
    unittest.main()
