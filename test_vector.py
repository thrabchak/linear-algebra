import unittest
import vector

class TestVectorMethods(unittest.TestCase):

    def assertDoubleEqual(self, a, b):
        self.assertTrue(abs(a-b) < vector.EPSILON)

    def test_create(self):
        v1 = vector.Vector([1,2,3])
        self.assertTrue(True)
    
    def test_create_empty(self):
        v1 = vector.Vector([])
        self.assertTrue(True)

    def test_equal(self):
        v1 = vector.Vector([1,2,3])
        v2 = vector.Vector([1,2,3])
        self.assertEqual(v1, v2)

    def test_not_equal(self):
        v1 = vector.Vector([1,2,3])
        v2 = vector.Vector([2,2,3])
        self.assertNotEqual(v1, v2)

    def test_plus(self):
        v1 = vector.Vector([1,2,3])
        v2 = vector.Vector([1,2,3])
        v3 = v1.plus(v2)
        expectedVector = vector.Vector([2,4,6])
        self.assertEqual(v3, expectedVector)

    def test_plus_decimals(self):
        v1 = vector.Vector([8.218, -9.341])
        v2 = vector.Vector([-1.129, 2.111])
        v3 = v1.plus(v2)
        expectedVector = vector.Vector([7.089, -7.230])
        self.assertEqual(v3, expectedVector)

    def test_minus(self):
        v1 = vector.Vector([1,2,3])
        v2 = vector.Vector([1,2,3])
        v3 = v1.minus(v2)
        expectedVector = vector.Vector([0,0,0])
        self.assertEqual(v3, expectedVector)

    def test_minus_decimals(self):
        v1 = vector.Vector([7.119, 8.215])
        v2 = vector.Vector([-8.223, 0.878])
        v3 = v1.minus(v2)
        expectedVector = vector.Vector([15.342, 7.337])
        self.assertEqual(v3, expectedVector)

    def test_minus_negative(self):
        v1 = vector.Vector([1,2,3])
        v2 = vector.Vector([2,4,3])
        v3 = v1.minus(v2)
        expectedVector = vector.Vector([-1,-2,0])
        self.assertEqual(v3, expectedVector)

    def test_scale_decimals(self):
        v1 = vector.Vector([1.671, -1.012, -0.318])
        v1.scale(7.41)
        expectedVector = vector.Vector([12.382, -7.499, -2.356])
        self.assertEqual(v1, expectedVector)

    def test_magnitude(self):
        v = vector.Vector([-.221, 7.437])
        self.assertTrue(abs(v.magnitude()-7.44028) < vector.EPSILON)

    def test_magnitude_3d(self):
        v = vector.Vector([8.813, -1.331, -6.247])
        self.assertTrue(abs(v.magnitude()-10.884) < vector.EPSILON)

    def test_unit_vec(self):
        v = vector.Vector([5.581, -2.136])
        v.normalize()
        expectedVector = vector.Vector([0.9339, -0.3574])
        self.assertEqual(v, expectedVector)

    def test_unit_vec_3d(self):
        v = vector.Vector([1.996, 3.108, -4.554])
        v.normalize()
        expectedVector = vector.Vector([0.340, 0.530, -0.7766])
        self.assertEqual(v, expectedVector)

    def test_normalize_zero(self):
        v = vector.Vector([0,0])
        v.normalize()
        self.assertEqual(v, vector.Vector([0,0]))

    def test_dot_product(self):
        v = vector.Vector([7.887, 4.138])
        v2 = vector.Vector([-8.802, 6.776])
        ans = -41.382
        self.assertDoubleEqual(v.dotProduct(v2), ans)

    def test_dot_product_3d(self):
        v = vector.Vector([-5.955, -4.904, -1.874])
        v2 = vector.Vector([-4.496, -8.755, 7.103])
        ans = 56.397
        self.assertDoubleEqual(v.dotProduct(v2), ans)

    def test_angle(self):
        v = vector.Vector([3.183, -7.627])
        v2 = vector.Vector([-2.668, 5.319])
        ans = 3.072
        self.assertDoubleEqual(v.angleBetween(v2), ans)

    def test_angle_3d(self):
        v = vector.Vector([7.35, 0.221, 5.188])
        v2 = vector.Vector([2.751, 8.259, 3.985])
        ans = 60.276
        self.assertDoubleEqual(v.angleBetween(v2, inRadians=False), ans)

    def test_parallel(self):
        v = vector.Vector([-7.579, -7.88])
        v2 = vector.Vector([22.737, 23.64])
        self.assertTrue(v.isParallel(v2))
        self.assertFalse(v.isPerpendicular(v2))

    def test_not_parallel_or_perpendicular(self):
        v = vector.Vector([-2.029, 9.97, 4.172])
        v2 = vector.Vector([-9.231, -6.639, -7.245])
        self.assertFalse(v.isParallel(v2))
        self.assertFalse(v.isPerpendicular(v2))

    def test_perpendicular(self):
        v = vector.Vector([-2.328, -7.284, -1.214])
        v2 = vector.Vector([-1.821, 1.072, -2.94])
        self.assertFalse(v.isParallel(v2))
        self.assertTrue(v.isPerpendicular(v2))

    def test_parallel_and_perpendicular_zero(self):
        v = vector.Vector([2.118, 4.827])
        v2 = vector.Vector([0, 0])
        self.assertTrue(v.isParallel(v2))
        self.assertTrue(v.isPerpendicular(v2))

    def test_parallel_and_perpendicular_both_zero(self):
        v = vector.Vector([0,0])
        v2 = vector.Vector([0, 0])
        self.assertTrue(v.isParallel(v2))
        self.assertTrue(v.isPerpendicular(v2))

    def test_projection(self):
        v = vector.Vector([3.039, 1.879])
        b = vector.Vector([0.825, 2.036])
        v2 = b.project(v)
        expectedVector = vector.Vector([1.083, 2.672])
        self.assertEqual(v2, expectedVector)

    def test_perpedicular_component(self):
        v = vector.Vector([-9.88, -3.264, -8.159])
        b = vector.Vector([-2.155, -9.353, -9.473])
        v2 = b.project(v)
        v3 = v.minus(v2)
        expectedVector = vector.Vector([-8.35, 3.376, -1.4337])
        self.assertEqual(v3, expectedVector)

    def test_projection_components(self):
        v = vector.Vector([3.009, -6.172, 3.692, -2.51])
        b = vector.Vector([6.404, -9.144, 2.759, 8.718])
        v2 = b.project(v)
        v3 = v.minus(v2)
        expectedParallelComponent = vector.Vector([1.9685, -2.81076, 0.84808, 2.6798])
        self.assertEqual(v2, expectedParallelComponent)
        expectedPerpendicularComponent = vector.Vector([1.04048, -3.3612, 2.8439, -5.1898])
        self.assertEqual(v3, expectedPerpendicularComponent)

    def test_cross_product(self):
        a = vector.Vector([5, 3, -2])
        b = vector.Vector([-1, 0, 3])
        v = a.crossProduct(b)
        expectedVector = vector.Vector([9, -13, 3])
        self.assertEqual(v, expectedVector)

    def test_cross_product_2(self):
        a = vector.Vector([8.462, 7.893, -8.187])
        b = vector.Vector([6.984, -5.975, 4.778])
        v = a.crossProduct(b)
        expectedVector = vector.Vector([-11.20457, -97.609, -105.6851])
        self.assertEqual(v, expectedVector)

    def test_area_of_parallelogram(self):
        a = vector.Vector([-8.987, -9.838, 5.031])
        b = vector.Vector([-4.268, -1.861, -8.866])
        v = a.crossProduct(b)
        area = v.magnitude()
        self.assertDoubleEqual(area, 142.122)

    def test_area_of_triangle(self):
        a = vector.Vector([1.5, 9.547, 3.691])
        b = vector.Vector([-6.007, 0.124, 5.772])
        v = a.crossProduct(b)
        area = v.magnitude()/2
        self.assertDoubleEqual(area, 42.564937)

if __name__ == '__main__':
    unittest.main()
