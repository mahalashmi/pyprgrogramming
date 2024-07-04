# def checktwolist():
#     list1 = [1,2,3,4]
#     list2 = [1,2,8,4]
#     x =len(list1)
#     y= len(list2)
#     for a in (0,x) and for b in (0,y):
#         if list1[x] == list2[y]:
#             print("same")
#         else:
#             print("not same")
    
# checktwolist()

def AreSame(x:list[int], y:list[int]) -> bool:
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return True