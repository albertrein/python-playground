import unittest
import fibonaci

class FibonacciTests(unittest.TestCase):
    
    def test_get_number_positional_fibonacci(self):
        fibonacci = fibonaci.Fibonacci()
        self.assertEqual(
            fibonaci.get_number_positional_fibonacci(5),
            8
        )