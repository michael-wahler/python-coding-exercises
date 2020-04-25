'''
Created on 23.04.2020

@author: Michael Wahler
'''
import unittest
from src.fizzbuzz import fizzbuzz1, fizzbuzz2 


class Test(unittest.TestCase):

    def test_fizzbuzz1(self):
        f = fizzbuzz1
        self.assertEqual(f(1), "1\n")
        self.assertEqual(f(2), "1\n2\n")
        self.assertEqual(f(3), "1\n2\nFizz\n")
        self.assertEqual(f(5), "1\n2\nFizz\n4\nBuzz\n")
        self.assertEqual(f(15), "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n")        

    def test_fizzbuzz2(self):
        f = fizzbuzz2
        self.assertEqual(f(1), "1\n")
        self.assertEqual(f(2), "1\n2\n")
        self.assertEqual(f(3), "1\n2\nFizz\n")
        self.assertEqual(f(5), "1\n2\nFizz\n4\nBuzz\n")
        self.assertEqual(f(15), "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n")        

    def test_compare (self):
        for i in range (1, 1000):
            self.assertEqual(fizzbuzz1(i), fizzbuzz2(i))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
