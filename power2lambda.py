terms = int(input("enter the number of terms: "))
result = list(map(lambda x: 2 ** x, range(terms)))
print("the total terms are:", terms)
for i in range(terms):
    print("2 raised to power", i, "is", result[i])


    '''output
    enter the number of terms: 4
the total terms are: 4
2 raised to power 0 is 1
2 raised to power 1 is 2
2 raised to power 2 is 4
2 raised to power 3 is 8
'''