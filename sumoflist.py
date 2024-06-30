def sum():
    list = [0,2,3,4,5]
    sum = 0
    #y = len(list)
    for a in range(len(list)-1,0,-1):
       sum += list[a] 
    print(sum)
    #print(y)
sum()