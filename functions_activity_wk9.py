
def cprg_max(x,y,z):

    if x<y:
        x = y
    if x<z:
        x = z
    return x


def myinfo (name, yob):
    age = 2025 - yob
    print ("Hello", name, "Your age is", age)




def my_sqrt (num):
    return num**0.5

print(cprg_max(7,8,9))
myinfo("Mary",2002)
print (my_sqrt(9))