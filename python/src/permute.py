'''
Created on 08.03.2020

@author: Michael Wahler
'''


def permute (alist, prefix = [], debug = False):
    """
    Returns a list of list with all permutations of the input list alist
    each sublist starts with the prefix followed by a permutation of alist

    Args:
        alist: the list to be permuted 
        prefix: the prefix of each sublist. needed for recursion

    Returns:
        a list of lists

    """    
    if debug:
        print ('{2}permute ({0}, {1})'.format (str(prefix), str(alist), '-' * len(prefix)), 'termination case' if 0==len(alist) else 'recursive case')
        
    if 0 == len (alist):
        return [prefix]
    
    else:
        result = []
         
        for i in range (0, len(alist)):
            first_half = alist[:i]        # alist up to position i
            second_half = alist [i + 1:]  # alist after position i+1
            
            if debug:
                print ('-' * len(prefix), "first_half:", first_half, "prefix: ", prefix, " second_half:", second_half)
                
            new_permutations = permute (first_half + second_half, prefix + [alist[i]], debug)
            
            result += new_permutations
            
        return result


if __name__ == '__main__':
    print (permute ([1, 2, 3, 4],debug=False))
    pass

