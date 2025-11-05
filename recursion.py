def fibo (n):

    if n <= 1:
        return n
    else:
         return fibo(n - 1) + fibo(n - 2)

nterms = int(input("enter the number of terms :"))
if nterms <= 0:
    print("please enter a positive number:")
else:
    print("fibonacci sequence:")
    for i in range(nterms):
        print (fibo(i))


'''output
        
enter the number of terms :6
fibonacci sequence:
0
1
1
2
3
5
'''