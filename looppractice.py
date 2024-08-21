def displayusingforloop():
    
    for x in range(1,11):
        print(x)
#displayusingforloop()

def displaynnumbers(n:int):
    for i in range(1,n):
        print(i)
#displaynnumbers(3)

def evennumber():
    for i in range(1,100):
        if i % 2 == 0:
            print(i)
#evennumber()
def findsquare(n:int):
    for i in range(1,n):
        square = i ** 2
        print(f"the square of {i} number {square}")
#findsquare(5)
def sumofnumber(n:int):
    i:int = 1 
    sum:int = 0
    while i<=n:
        sum = sum + i
        i += 1
    print(sum)
#sumofnumber(3)
def displaymultiplicationtable(n:int):
    for i in range(1,11):
        multiply =i*n
        print(f"{i}*{n}={multiply}")
#displaymultiplicationtable(3)
def factorial(n:int):
    fact:int = 1
    for i in range(1,n+1):
        fact = fact* i
    print(fact)
#factorial(5)



