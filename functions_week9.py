
'''
def my_max():
    print("Please enter two numbers")
    x = float(input())
    y = float(input())

    if x<y:
        print(y)
    else:
        print(x)
    
print("welcome to functions ")

   
my_max()
my_max()
my_max()
print("Random Messages")
my_max()
'''
#the function must do something
#the output of a function is the value of an expression

'''
x = print(3)
print(x)
print(print(3))
'''

'''def fun_name():
    #statement
    #statement
    #statement
    return  #this is the value/output of a function'''
'''
def my_max(x,y):
    max = y
    if x>y:
        max = x
    return max

print(my_max(3,4))
m = my_max(4,5)
print(m)

l = 4
n = 33
m = my_max(l,n)

print(m)
'''

#input (arguments) - output (return) function


def square(x):
    y = x**2
    return y
print(square(5))


#input (arguments) - no output

x = print("hello")
print(x)

#no input (no argument), but you have a return (output)

print("Please provide your name")
name = input()
print("Hello", name)