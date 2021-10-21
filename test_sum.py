import unittest
from main import k
import math

class TestSum(unittest.TestCase):

    def test_k(self):
        self.assertAlmostEquals(k(0.3,0.0000001),math.pi / 2 - math.atan(0.3))