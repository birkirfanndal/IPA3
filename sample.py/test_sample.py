import unittest
from sample import fizzbuzz

class SampleTest(unit.TestCase):
    def fizz_test(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        