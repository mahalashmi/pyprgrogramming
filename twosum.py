def twosum():
    num=[2,7,11,1]
    target=13
    for i in range( 0,len(num)):
        for y in range(i+1,len(num)):
            if(num[i]+num[y]== target):
                print(i,y)
            
twosum()
