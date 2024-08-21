def power_to_raise(base_num,power_num):
    result = 1
    for i in range(power_num):
        result = result*base_num
    return result
    
print(power_to_raise(3,4))