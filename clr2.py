list1=input("enter the color list 1(sep with space) : ").split()
list2=input("enter the color list 2(sep with space) : ").split()
result=[]
for color in list1:
    if color not in list2:
        result.append(color)
print(result)
