import unittest
import line
import vector

V = vector.Vector
L = line.Line

class TestLineMethods(unittest.TestCase):

    def assertDoubleEqual(self, a, b):
        self.assertTrue(abs(a-b) < vector.EPSILON)

    def test_create(self):
        norm = V([1,2])
        l = L(norm, 1)
        self.assertTrue(line != None)

    def test_parallel(self):
        n1 = V([3, -2])
        l1 = L(n1)
        n2 = V([-6, 4])
        l2 = L(n2)
        self.assertTrue(l1.isParallel(l2))

    def test_not_parallel(self):
        n1 = V([1, 2])
        l1 = L(n1)
        n2 = V([1, -1])
        l2 = L(n2)
        self.assertFalse(l1.isParallel(l2))

    def test_equal(self):
        n1 = V([2, 2])
        l1 = L(n1, 5)
        n2 = V([1, 1])
        l2 = L(n2, 5)
        self.assertNotEqual(l1, l2)

    def test_not_equal(self):
        n1 = V([-1, -1])
        l1 = L(n1, 5)
        n2 = V([1, 1])
        l2 = L(n2, 5)
        self.assertNotEqual(l1, l2)

    def test_intersect1(self):
        n1 = V([4.046, 2.836])
        l1 = L(n1, 1.21)
        n2 = V([10.115, 7.09])
        l2 = L(n2, 3.025)
        (a, b) = l1.intersect(l2)
        self.assertEqual(a, "SAME_LINE")

    def test_intersect2(self):
        n1 = V([7.204, 3.182])
        l1 = L(n1, 8.68)
        n2 = V([8.172, 4.114])
        l2 = L(n2, 9.883)
        (a, b) = l1.intersect(l2)
        self.assertEqual(a, "INTERSECTION")
        self.assertEqual(b, V([1.173, 0.073]))

    def test_intersect3(self):
        n1 = V([1.182, 5.562])
        l1 = L(n1, 6.744)
        n2 = V([1.773, 8.343])
        l2 = L(n2, 9.525)
        (a, b) = l1.intersect(l2)
        self.assertEqual(a, "NO_INTERSECTION")

if __name__ == '__main__':
    unittest.main()
