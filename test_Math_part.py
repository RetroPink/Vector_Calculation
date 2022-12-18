import unittest
from Math_part import vectors_sum
from Math_part import product_vectors_vector
from Math_part import vectors_difference
from Math_part import vector_multiplication_scalar
from Math_part import product_vectors_scalar
from Math_part import vector_modulus
from Math_part import vector_division_scalar


class Test_Math_part(unittest.TestCase):
    def test_vectors_sum(self):
        self.assertEqual(vectors_sum([1, 3, 4], [7, 8, 3]), [8, 11, 7])
        self.assertEqual(vectors_sum([1, 3], [7, 8, 3]), [8, 11, 3])
        self.assertEqual(vectors_sum([1, 3, 4], [7, 8]), [8, 11, 4])
        self.assertEqual(vectors_sum([1.1, 2.2, 3.3], [4.4, 5.5, 6.6]), [5.5, 7.7, 9.9])

    def test_product_vectors_vector(self):
        self.assertEqual(product_vectors_vector([1, 3, 4], [7, 8, 3]), [-23, 25, -13])
        self.assertEqual(product_vectors_vector([1, 2, 3], [7, 8, 0]), [-24, 21, -6])
        self.assertEqual(product_vectors_vector([7, 8, 0], [1, 2, 3]), [24, -21, 6])
        self.assertEqual(product_vectors_vector([10, 75, 100], [7, 8]), [-800, 700, -445])
        self.assertEqual(product_vectors_vector([1.1, 2.2, 3.3], [4.4, 5.5, 6.6]), [-3.63, 7.26, -3.63])
        self.assertEqual(product_vectors_vector([1, 2, 3, 4], [5, 6, 7, 8]), 70)
        self.assertEqual(product_vectors_vector([1, 2, 3], [5, 6, 7, 8]), 38)
        self.assertEqual(product_vectors_vector([1, 2, 3, 4], [5, 6, 7]), 38)
        self.assertEqual(product_vectors_vector([1, 2], [5, 7, 8]), [16, -8, -3])
        self.assertEqual(product_vectors_vector([2, 3, 4], [5, 6]), [-24, 20, -3])
        self.assertEqual(product_vectors_vector([2, 3], [5, -6, 7, 8.3]), -8.0)

    def test_vectors_difference(self):
        self.assertEqual(vectors_difference([1, 3, 4], [7, 8, 3]), [-6, -5, 1])
        self.assertEqual(vectors_difference([8, 7], [1, 2, 3]), [7, 5, -3])
        self.assertEqual(vectors_difference([10, 75, 100], [7, 8]), [3, 67, 100])
        self.assertEqual(vectors_difference([1.1, 2.2, 3.3], [4.4, 5.5, 6.6]), [-3.3, -3.3, -3.3])

    def test_vector_multiplication_scalar(self):
        self.assertEqual(vector_multiplication_scalar([1, 6, 3], 2), [2, 12, 6])
        self.assertEqual(vector_multiplication_scalar(2, [1, 6, 3]), [2, 12, 6])
        self.assertEqual(vector_multiplication_scalar([1.1, 8.4, 7.6], 10), [11, 84, 76])
        self.assertEqual(vector_multiplication_scalar(-2, [1, 6, 3]), [-2, -12, -6])

    def test_product_vectors_scalar(self):
        self.assertEqual(product_vectors_scalar([7, 3, 5], [4, 9, 2]), 65)
        self.assertEqual(product_vectors_scalar([7.5, 3, 5.3], [4, 9.2, 2.1]), 68.73)
        self.assertEqual(product_vectors_scalar([7.5, -3, -5.3], [-4, 9.2, -2.1]), -46.47)

    def test_vector_modulus(self):
        self.assertEqual(vector_modulus([3, 8, 9]), round(12.409673645990857, 10))
        self.assertEqual(vector_modulus([8, 9, -10]), round(15.652475842498529, 10))
        self.assertEqual(vector_modulus([4.6, 7.3, 1.5]), round(8.757853618324527, 10))

    def test_vector_division_scalar(self):
        self.assertEqual(vector_division_scalar([2, 6, 8], 2), [1.0, 3.0, 4.0])
        self.assertEqual(vector_division_scalar([2, 6, 8], 0.5), [4.0, 12.0, 16.0])
        self.assertEqual(vector_division_scalar([-2, 6, 8], -1), [2.0, -6.0, -8.0])
