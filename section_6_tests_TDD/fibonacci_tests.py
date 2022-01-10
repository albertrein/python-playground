import unittest
from fibonacci import Fibonacci

class FibonacciTests(unittest.TestCase):
    
    def test_get_number_positional_fibonacci(self):
        fibonacci = Fibonacci()
        self.assertEqual(
            fibonacci.get_number_positional_fibonacci(5),
            8
        )
        self.assertNotEqual(
            fibonacci.get_number_positional_fibonacci(6),
            21
        )
        self.assertLessEqual(
            fibonacci.get_number_positional_fibonacci(0),
            1
        )

if __name__ == '__main__':
    unittest.main()