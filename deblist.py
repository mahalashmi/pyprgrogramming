def sum_fn(x:int):
    result=0
    for i in range(x):
        result+=i
    return result

final_result = sum_fn(10)
print(final_result)