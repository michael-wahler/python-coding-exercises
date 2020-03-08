'''
Created on 08.03.2020

@author: Michael Wahler
'''
import unittest
import math
from src.permute import permute


def permutationLength (original_list, permutations, debug = False):
    orig = len (original_list)
    perms = len (permutations)
    if debug:
        print ('  {0} = {1}!'.format(perms, orig))
    return perms == math.factorial (orig)


class Test(unittest.TestCase):

    def testSimplePermutations(self):
        self.assertEqual(permute([]), [[]], '')
        self.assertEqual(permute([1]), [[1]], '')
        self.assertEqual(permute([1, 2]),
                         [[1, 2],
                          [2, 1]], '')
        
        self.assertEqual(permute([1, 2, 3]),
                        [ [1, 2, 3],
                          [1, 3, 2],
                          [2, 1, 3],
                          [2, 3, 1],
                          [3, 1, 2],
                          [3, 2, 1]],
                        'oops')
        
    def testPermutationLength (self):
        test_lists = [ [],
                      [1],
                      [1, 2],
                      [1, 2, 3],
                      [1, 2, 3, 4],
                      [1, 2, 3, 4, 5],
                      [1, 2, 3, 4, 5, 6]
                    ]
        
        for l in test_lists:
            self.assertTrue(permutationLength(l, permute(l, [], False)))
        
    def testRandomLists (self):
        pass
        # TODO: generate random list, check length, check if each element of the result is a permutation, check for no duplicates?
                        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testPermutations']
    unittest.main()
