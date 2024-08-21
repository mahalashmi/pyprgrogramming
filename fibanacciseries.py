
def fib(n:int):
    list1 = [0,1]
    a = 2
    while(a<=n):
        list1.append(list1[a-2]+list1[a-1])
        a+=1
    print(list1)

fib(6)