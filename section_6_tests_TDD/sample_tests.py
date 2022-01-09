import unittest
from sample_class import Sample

class SampleTests(unittest.TestCase):
    def test_samples_sucess(self):
        sample = Sample()
        self.assertEqual(
            sample.samples_sucess(),
            True
        )

    def test_samples_fail(self):
        sample = Sample()
        self.assertEqual(
            sample.samples_fail(),
            False
        )

if __name__ == '__main__':
    unittest.main()