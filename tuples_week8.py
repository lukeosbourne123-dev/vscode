data = () #cannot be modified because it is immutable
data = (1,2,3,4)
print(type(data))

weekend = ("Sat,Sun") #why is this a string? not a tuple - the comma is inside the ""
day = ("Mon",) 
print(type(day))

x = 3
x = (4,)
print (type(x))
print(day[0])

for day in weekend:
    print(day, end="\t")
#weekend[0] = 'Fri' error - immutable
#weekend.append("Tue") error not supported

print()

age = 13
name = "John"
city = "Calgary"

info = (name, age, city)
print(info)

info_list = [name, age, city]
print(info_list)

print()

objects = ("Car", 1, 3.4, True)
device = objects[0]
count = objects[1]
measurement = objects[2]
status = objects[3]
#unpack
device, count, measurement, status = objects
print(device, count, measurement, status)

objects_ = list(objects)
objects_again = tuple(objects_)
print(objects_, objects_again)

#concat tuples
num1 = (1,2,3)
num2 = (4,5,6)
num3 = num1 + num2
print (num3)

#num1.extend() error immutable

#del num3[2] error immutable

print(num3[:3])
print(num3[3:])
del num3


