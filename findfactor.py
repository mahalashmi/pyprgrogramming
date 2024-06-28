def factor(x:int,y:int):
    z = x % y
    if z == 0:
        print("x is factor of y")
    else:
        print("x is not factor of y")
factor(10,3)