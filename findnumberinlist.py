def findx():
    x = int(input("Enter any value from list"))
    list = [1,2,3,4]
    for a in range(0,len(list)):
        if(list[a]==x):
            print("x is found")
            return
    else:
        print("not found")
findx()