'''
Created on 23.04.2020

@author: Michael Wahler
'''


def fizzbuzz1 (n):
    result = ''
    for i in range(1, n + 1):
        x = ''
        if i % 3 == 0:
            x = "Fizz"
        if i % 5 == 0:
            x += "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            x = str (i)
        result += (x + "\n")
    return result


def fizzbuzz2 (n):
    result = ''
    for i in range(1, n + 1):
        x = ''
        if i % 3 == 0:
            x = 'Fizz'
        if i % 5 == 0:
            x += 'Buzz'
        if '' == x:
            x = str(i)
        result += (x + "\n")
    return result
        

if __name__ == '__main__':
    print (fizzbuzz1(16))
    print ("------------------------")
    print (fizzbuzz2(16))
         
