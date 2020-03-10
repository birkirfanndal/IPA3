import unittest
from sample import fizzbuzz

class SampleTest(unittest.TestCase):
    def fizz_test(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(12), "Fizz")
        self.assertEqual(fizzbuzz(18), "Fizz")

        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")
        self.assertEqual(fizzbuzz(35), "Buzz")
        self.assertEqual(fizzbuzz(40), "Buzz")

        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")
        self.assertEqual(fizzbuzz(60), "FizzBuzz")


        self.assertEqual(fizzbuzz(2),2)
    

if __name__ == "__main__":
    unittest.main()
