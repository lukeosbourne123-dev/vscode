print ("Sum from 1 to 100")

number = 0
sum = 0

while number <100:
    number += 1
    sum += number
print(sum)


'''
print("factorial of 5")

number = 0
fact = 1

while number <5:
    number+=1
    fact *= number
print(fact)
'''


print ("Welcome to the quad equation solver")
option = "Y"
while option == "Y":
    print("please enter 3 numbers: a, b, c")

    a = float(input("\n"))
    b = float(input("\n"))
    c = float(input("\n"))
    x1 = x2 = None
    if a == 0:
        if b == 0:
            print("No solution")
        else: 
            x1 = x2 = -c/b
    else:
        det = b**2 - 4*a*c # det (determinant)
        if det >= 0:
            x1 = (-b + (det) **0.5)/(2*a)
            x2 = (-b - (det) **0.5)/(2*a)
            print("Solution: ", x1,x2)
        else:
            print("No real solution")
    option = input("Do you want to contine?Y/N\n")
    
