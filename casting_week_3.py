# this is is our 3rd class
'''
multi-line comment 3 ' above and below
'''

# Review
# Assignment 

# write 4 assignment statements for int, float, boolean, string; print; print type

x = 10+2
y = 7.9
q = True
msg = "Hi i am a new CPRG student"

print("the value of the variable x is: ",x,"and the type is ",type(x))
print("the value of the variable y is: ",y,"and the type is ",type(y))
print("the value of the variable q is: ",q,"and the type is ",type(q))
print("the value of the variable msg is: ",msg,"and the type is ",type(msg))


# casting - changing from one type to another; from int to float is promoting(increasing the size); from float to int is demoting(decreasing in size)

#some function call: print, input, int, float, str, bool
num_as_text = "43"
num_as_num = int(num_as_text) #converting string (text) to num

print(num_as_text) #will print as text
print(num_as_num) # will it print? No
print(str(num_as_num)) # equivalent

num = 3


# using input function. note input function always return a string (text)

'''user_input = input("Please enter your year of birth\n")
year_of_birth = int(user_input)
print("Your age is ",2025 - int (year_of_birth))
'''


# print function - working with a separator 

print("Hello","world", sep=',', end=' ')
print("Hello","world", sep=' ')
print("Hello\tworld") # \t tab
print("Hello\nworld") # \n sends to a new line
print('What is the student\'s name?')
print('Use this symbol \\ to make an escape character') # "\\" to prints a "\" refer to powerpoint slide

# precedence rules - BODMAS, read left to right

expression = 3+4*0-300+12/3
print(expression)

expression_2 = 4/2*3

print(expression_2)

# More about assignment 

x = 3 
x = x+5
print(x)

# can we have a shorthand for this expression?\
x += 5 # x = x+5
print(x)
#other operations

x -= 2 # x = x-2
print(x)
x *= 3 # x = x*3
print(x)
x /= 2 # x = x/2
print(x)
x **= 4 # x = x ** 4
print(x)