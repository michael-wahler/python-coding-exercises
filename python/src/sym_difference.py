'''
Created on 21.06.2020

@author: Michael Wahler
'''


def symmetric_difference (set_a, set_b):
    return set_a.difference(set_b).union(set_b.difference(set_a))
    return result


if __name__ == '__main__':
    print (symmetric_difference (set(),set()))
    print (symmetric_difference ({1},set()))
    print (symmetric_difference ({1},{2}))
    print (symmetric_difference ({1},{3}))
    print (symmetric_difference ({1,2},{2,3}))
    

def read_from_console(): # reads two lines with space-separated numbers
    slist1 = input().split() # list ['5', '4', '3', '2']
    #  use the map() method to convert all the strings to integers.
    list1 = list(map(int, slist1)) # [5, 4, 3, 2]
    slist2 = input().split() # list ['5', '4', '3', '2']
    list2 = list(map(int, slist2)) # [5, 4, 3, 2]

    print (symmetric_difference (set (list1), set (list2)))
