'''
Created on Sep 14, 2020

@author: mike
'''
import unittest


def xy ():
    return (42,23)


class Test(unittest.TestCase):


    def testTuples(self):
        (x1, y1) = xy ()
        
        coords = xy ()
        
        x2 = coords[0]
        y2 = coords[1]
        
        self.assertEqual(x1, x2)
        self.assertEqual(y1, y2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTuples']
    unittest.main()