def multiples3():
    m = int(input("Enter m value:"))
    n = int(input("Enter n value:"))
    while(m<=n):
       z = m*3
       if(z > n):
           break
       else:
           print(z)
           m+=1
#multiples3()
def multiplesof7():
    m = int(input("Enter m:"))
    n = int(input("Enter n:"))
    while(n >= m):
        z = n * 7
        if (z > n):
            print(z)
            n -= 1
multiplesof7()