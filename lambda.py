area1 = lambda x: x * x
area2 = lambda x, y: x * y
area3 = lambda x, y: 0.5 * x * y
a= int(input("enter the length of the square: "))
print("area of the square is", area1(a))
l = int(input("enter the length of the rectangle: "))
w = int(input("enter the width of the rectangle: "))
print("area of the rectangle is", area2(l, w))
h = int(input("enter the height of the triangle: "))
b = int(input("enter the base of the triangle: "))
print("area of the triangle is", area3(h, b))

'''output
enter the length of the square: 5
area of the square is 25
enter the length of the rectangle: 6
enter the width of the rectangle: 4
area of the rectangle is 24
enter the height of the triangle: 10
enter the base of the triangle: 8
area of the triangle is 40.0
'''