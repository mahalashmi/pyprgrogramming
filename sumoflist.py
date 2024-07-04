def sum():
    list = [0,2,3,6,4,5]
    sum = 0
    average = 0
    #y = len(list)
    for a in range(len(list)-1,0,-1):
       sum += list[a] 
       
    print(sum)
    average = sum/len(list)
    print(average)
    median = len(list)/2
    print(median)
    #print(y)
sum()