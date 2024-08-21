def listadd(k:int)->bool:
    arr = [2,3,6,1,3,6]
    for x in range(0,len(arr)):
        for y in range(x + 1,len(arr)):
            if arr[x]+arr[y] == k:
                print(x)
                print(y)
                return True
            
    return False  

#print(listadd(77))
def listdict(k:int):
    arr:list[int] = [3,4,8,1,2,4,6] # int[] arr = new int[10];
    b={}
    '''
    dict ={"name":"magi",
           "age":35}
    dict['city']='panruti'
    #del dict['age'][]
    
    
    print(dict.get('name'))
    length=len(dict)
    print(length)
    for i,j in dict.items():
        print(f"{i}:{j}")
    '''
    for i in arr:
        b[i]=True
    print(b)
listdict(3)
