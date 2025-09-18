num=input("enter a list of integers sep by space : ").split()
result=[]
for n in num:
    n=int(n)
    if n > 100:
        result.append("over")
    else:
        result.append(n)
print(result)