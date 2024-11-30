'''
Created on May 12, 2021

@author: mike
'''


def foobar (myfunc):
    def wrapper (x):
        print ("foo")
        myfunc (x)
        print ("bar")
    return wrapper
    
    
@foobar
def g (i):
    print ("g({})".format(i)) 


    
    
    
class C:
    def __init__ (self, i):
        self.x = i
        
        
        
if __name__ == '__main__':
    g (15)
    c0 = C(0)
