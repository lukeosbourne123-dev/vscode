# If statement
# if (keyword, is a must)
# boolean expression (Is a must, as it states whether a condition is true or false)
# : (IS A MUST, it means "then")
# indentation (MUST HAVE)
# one or more statements of any type



#if else statement - elif
# if (keyword, is a must)
# boolean expression (Is a must, as it states whether a condition is true or false)
# indentation (MUST HAVE)
# : (IS A MUST, it means "then")
# one or more statements of any type
#non indented else (optional)
# : (is a must after else)
#if else works fine if we have two conditions



'''myage = 25
if myage == 25:
    print("25 is Luke's age")
else:
    print("that is not Luke's age")
'''

'''
print("Welcome to the software dev party")
name = input ("Please Enter your name: \n")
if name == 'Luke':
    name = 'Luke'

print("Welcome, ", name)

print("To have a drink you must provide your age")

age = int(input("What is your age?"))

is_adult = age >=18

if is_adult:
    print("You are allowed to drink")
else: 
    print ("You are not allowed to drink")
'''

print("Welcome to the grade system")
grade = int(input("Please Enter your grade\n"))

if grade >= 90:
    letter_grade = 'A'
elif grade>= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
   
print("Your letter grade is", letter_grade)