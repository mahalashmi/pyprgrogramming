def displaychar():
    letter = ['a','b','n']
    for i in range(len(letter)):
        print(letter[i])
#displaychar()

#Copy the contents of string to char array. 
def copystringtochar():
    str = "magi"
    chararray = []
    for x in str:
        chararray.append(x)
    print(chararray)
#copystringtochar()

#38. Check if a char is present in char array. 

def checkcharinlist(x:int):
    chararray = ['c', 'f', 'k']
    for a in range(0,len(chararray)):
        if x == chararray[a]:
            print("True")
            return
    
    print("false")

'''
def checkcharinlist():
    chararray = ['f', 'h','j']
    x = ch(input("Enter any char from list"))
    for a in range(0,len(chararray)):
        if x == a[chararray]:
            print("Char found")
    print("not found")
'''
#checkcharinlist('c')
# 39. Check the number of times a char occurs in the char array. 

# def charoccurance():
#     list = ['a','b','c','a','a']
#     count = 0
    
#     for a in range(0,len(list)):  
        
#         for b in range(1,len(list)):
#             if list[a] == list[b] :   
#                 count += 1
#             else:
#                 count +=0
#         b += 1       
        
#     print(count)
# charoccurance()

def charcount(x:list[str]) -> dict[str, int]:
    result:dict[str, int]={}
    for i in x:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result


res:dict[str, int] = charcount(['a','a','c','c','c'])
for k, v in res.items():
    print(f"{k=} {v=}")
for v in res.values():
    maxvalue = 0

    if  maxvalue < res[v]:
        maxvalue = res[v]
    else:
        maxvalue > res[v]
        print(maxvalue)
    