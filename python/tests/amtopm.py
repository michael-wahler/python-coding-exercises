'''
Created on Jun 16, 2020

@author: chmiwah
'''
import unittest
from src.amtopm import timeConversion


 


class Test(unittest.TestCase):
    

    def testPositives(self):
        self.assertEqual(timeConversion('12:00:00AM'), '00:00:00')
        self.assertEqual(timeConversion('12:59:00AM'), '00:59:00')
        self.assertEqual(timeConversion('01:00:00AM'), '01:00:00')
        self.assertEqual(timeConversion('11:59:59AM'), '11:59:59')
        self.assertEqual(timeConversion('12:00:00PM'), '12:00:00')
        self.assertEqual(timeConversion('12:59:00PM'), '12:59:00')
        self.assertEqual(timeConversion('01:00:00PM'), '13:00:00')
        self.assertEqual(timeConversion('11:59:59PM'), '23:59:59')

    def testNegatives (self):
        self.assertRaises(Exception, timeConversion, '13:00:00AM')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConversion']
    unittest.main()