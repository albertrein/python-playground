import unittest

from maxCost import maxCost

class MaxCostTests(unittest.TestCase):

    def tests_maxCost(self):
        self.assertEqual(
            maxCost([5,2,5,3,11,1,5], ['legal','ilegal','legal','ilegal','legal'],2),
            10
        )
        
        self.assertEqual(
            maxCost([5, 0, 3, 2, 3, 4, 5], ['legal','legal','illegal','legal','legal'],1),
            5
        )

if __name__ ==  '__main__':
    unittest.main()