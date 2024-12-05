import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import calculate_mortgage

class TestMortgageCalculator(unittest.TestCase):
    def test_calculate_mortgage(self):
        self.assertAlmostEqual(calculate_mortgage(300000, 5, 30), 1610.46, places=2)
        self.assertAlmostEqual(calculate_mortgage(100000, 3, 15), 690.58, places=2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_mortgage("invalid", 5, 30)
            print("123123")

if __name__ == '__main__':
    unittest.main()
