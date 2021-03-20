l=int(input("ENTER LENGTH:"))
b=int(input("ENTER BREADTH:"))
h=int(input("ENTER HEIGHT:"))
x = lambda a : a * a
print("AREA OF SQUARE IS ",(x(l)))
y = lambda a, b : a * b
print("AREA OF RECTANGLE IS ",(y(l, b)))
z = lambda a, b : 1/2 * (a * b)
print("AREA OF TRIANGLE IS ",(z(b, h)))
