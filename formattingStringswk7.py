#The print function can take several argument

'''
name1 = "John"
name2 = "Mary"
name3 = "Paul"

print(name1, name2, name3, sep= "\t")
'''
'''
print(format(12345.6789, ".2f"))
print(format(1212222111.2236565, ".2e"))
print(format("Hello", "s"))
print(format(0.33, "%"))
print(format(124, "d"))

msg = format (12345.6789, ".2f")
print (msg)
'''

# second form of format
"hello".format()

'''
x = 3
y = 4.3
z= 4.53131
print("The value of x is", x, "The value of y is", y)
print("The value of y is {1:.3f} and the value of x is {0:.2e}".format(x, y))

#third way to format string

print(f"x is {x:d}, y is {y:4f}")
print(f"x is binary {x:x}")
name1 ="John"
name2 = "Joseph"
age1 = 20
age2 = 21

print(f"{name1:>20s} {age1:d}")
print(f"{name2:>20s}{age2:d}")
'''


yesterday_value = 0.7588
today_value = 0.7479
change = today_value - yesterday_value

print(f"{"Exchange":^24}")
print(f"{"Date":>10s}{"Rate":>10s}")
print(f"{"Yesterday":>10s}{yesterday_value:>10.4f}")
print(f"{"Today":>10s}    {today_value}")
print(f"{"Change":>10s}   {change:>.4f}")

# >10s - 10 spaces to the right
#REVIEW - 3 types of formatting

# format()
# "".format
# f""


num = 152525.23568
print(f"{num:.2e}")

name = "Luke"
age = 25
gpa = 3.999999
text = "The name is {0:s}, the gpa is {2:.0f}, the age is {1:d}".format(name, age, gpa)
print(text)
# :s - string  :f - Float   :d - decimal

text = f"The name is {name:s}, the gpa is {gpa:.0f}, the age is {age:d}"
print("text")


names = ["John", "Sam", "Cassandra", "Tom", "Sarah", "Michael"]
GPA = [3.4,3.6,3.1,3.6,3.8,4.0]
print(f"{"GPA Table":^22}")
print(f"{"Name":>10s}{"GPA":>6s}")
print(f"{"====":>10s}{"====":>6s}")
for i,j in zip(names,GPA):
    print(f"{i:>10s}{j:>6.0f}")