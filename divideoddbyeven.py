def oddbyeven(a:int, b:int)->int:
    if a % 2 == 1 and b % 2 == 0:
        c = a / b
        return c
    
print(oddbyeven(9,2))
