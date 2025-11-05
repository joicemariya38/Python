def check(n):
    if n% 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("enter the number:"))
print("the given number",num, "is", check(num))

'''
output
enter the number:31
the given number 31 is odd
enter the number:42
the given number 42 is even
'''