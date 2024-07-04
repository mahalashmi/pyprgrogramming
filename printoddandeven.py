
def displayodd(a:int,b:int):

    while(a <= b):
        if (a % 2 )==1:
            print(a)
        a +=1

#displayodd(0,100)
def displayeven(x:int, y:int):
    while(x <= y):
        if(x % 2 )==0:
            print(x)
        x += 1

#displayeven(0,100)

def displayodddown(a:int, b:int):
    while(a >= b):
        if(a % 2)== 1:
            print(a)
        a -= 1
#displayodddown(100,0)

def displayevendown(x:int,y:int):
    while(x >= y):
        if (x % 2)==0:
            print(x)
        x -= 1
#displayevendown(100,0)
    
def oddnumber(x:int):
    y = input("enter n:")
    #print(y)
    while(x <= int(y)):
        if(x % 2)==1:
            print(x)
        x += 1
#oddnumber(0)
def evennumber(x:int):
    y = int(input("Enter n:"))
    while(y >= x):
        if(y % 2)==0:
            print(y) 
        y -=1
evennumber(0)
    


#x = input("getInput:  ")
#print(x)

def isEven(x:int) -> bool:
    if x%2 == 0:
        return True
    return False

def printallEven(start:int, end:int):
    for i in range(start, end):
        if isEven(i):
            print(i)

def printallOdd(start:int, end:int):
    for i in range(start, end):
        if isEven(i) == False:
            print(i)

printallEven(0, 100)
printallOdd(0, 100)


    