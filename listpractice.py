def displaylist():
    list = [12,2,33,4,5]
    
    #list.append(5)
    #list.remove(12)
    min = 0
    
    list.sort()
    for i in range(0,len(list)):
        print(list[i])
displaylist()
def reverselist(list):
    for i in reversed(list):
        print(i)
#reverselist(list=[1,2])
def find_max_inlist(num):
    max:int = 0
    for x in num:
        if x >max:
            max = x
        else:
            x = max
    print(max)
#find_max_inlist(num = [0,0])
