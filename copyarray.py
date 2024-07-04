def copylist():
    list1 = [1,2,3,4]
    list2 = []
    for x in list1:
        list2.append(x)
    print(list2)
#copylist()
def copyreverse():
    list1= [2,3,4,5]
    list2= []
    for x in reversed(list1):
        list2.append(x)
    print(list2)
#copyreverse()

def reverselist():
    numlist = [22,33,44,55]
    
    for x in (reversed(numlist)):
        print(x)
    print(numlist)
reverselist()

