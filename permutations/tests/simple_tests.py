'''
Created on 08.03.2020

@author: Michael Wahler
'''
import unittest
import math
from src.permute import permute


def permutationLength (original_list, permutations):
    orig = len (original_list)
    perms = len (permutations)
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
            self.assertTrue(permutationLength(l, permute(l)))
        
        # self.assertTrue(permutationLength([1], [[1]]))
                        
#     def testSimple(self):
#         i = 1
#         mylist = [1, 2, 3, 4]
#         first_half = mylist[:i]
#         second_half = mylist[i + 1:]
#         print (first_half)
#         print (mylist[i])
#         print (second_half)
# 
#         x = [1, 2]
#         y = [3, 4]
#         print (x + y)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testPermutations']
    unittest.main()
