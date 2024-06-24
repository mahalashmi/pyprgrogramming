def genodd(x:int) -> list:
    result:list = []
    for i in range(x):
        if i%2==1:
            result.append(i)
    return result