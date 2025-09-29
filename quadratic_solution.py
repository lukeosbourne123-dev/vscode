print ("Welcome to the quadratic solution")
print ("Please enter three numbers a, b, c")

a = float(input('\n'))
b = float(input('\n'))
c = float(input('\n'))
x1 = 0
x2 = 0

if a == 0:
    x1 = -b/c
    x2 = -b/c

else: 
    if b**2 >= 4*a*c:
        x1 = (-b + (b**2 - 4*a*c)** 0.5)/(2*a)
        x2 = (-b + (b**2 - 4*a*c)** 0.5)/(2*a)
    else:
        x1 = None
        x2 = None
if x1 == None:
    print(" There is no solution in the real domain. :(")
else:
    print ("The solution to this problem is ", x1, x2)
    