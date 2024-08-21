import sys
print(sys.getrecursionlimit())
def fib(n:int):

    x = 0
    y = 1
    a = 1
    print(x)
    print(y)

    while(a<=n):
        count = x+ y
        x = y
        y = count
        print(count)
        a+=1
fib(5)

def recursion(n:int):
    
    

