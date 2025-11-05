def calculate(p, n, r):
    s =(p * n * r)/100
    print("simple interest =", s)

age = int(input("enter the age:"))
p = int(input("enter the principal amount:"))
n = int(input("enter the number of years:"))

if age < 60:
    r=10
else:
    r=12

print("rate of interest:",r)
calculate(p, n, r)


'''output
enter the age:65
enter the principal amount:20000
enter the number of years:3
rate of interest: 12
simple interest = 7200.0

enter the age:25
enter the principal amount:10000
enter the number of years:2
rate of interest: 10
simple interest = 2000.0

'''
