def primenumber():
    x = int(input("enter number"))
    for a in range(2,x):
        if x % a ==0:
            print("not prime")
            return
    print("prime") 
             
    
        
primenumber()