'''
Created on 08.03.2020

@author: Michael Wahler
'''


# parameter: a list [1,2,3]
# result: a list of lists [[1,2,3],[1,3,2],...]
def permute (myList):
    return permute_prefix ([], myList)


# returns a list of list; each sublist starts with prefix followed by a
# permutation of rest_list
# arguments: prefix: a list
#            rest_list: a list
def permute_prefix (prefix, rest_list, debug = False):
    if debug:
        print ('{2}permute_prefix ({0}, {1})'.format (str(prefix), str(rest_list), '-' * len(prefix)))
        
    if 0 == len (rest_list):
        return [prefix]
    
    elif 1 == len (rest_list):
        return [ prefix + rest_list ]
    
    else:
        result = []
         
        for i in range (0, len(rest_list)):
            first_half = rest_list[:i]
            second_half = rest_list [i + 1:]
            new_permutations = permute_prefix (prefix + [rest_list[i]], first_half + second_half)
            result += new_permutations
            
        return result


if __name__ == '__main__':
    print (permute ([1, 2, 3, 4]))

