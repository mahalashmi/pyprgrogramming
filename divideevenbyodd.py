def evenbyodd(a:int, b:int)->int:
    if a % 2 == 0 and b % 2 == 1:
       c =  a / b
       return c
    
print(evenbyodd(10,7))
