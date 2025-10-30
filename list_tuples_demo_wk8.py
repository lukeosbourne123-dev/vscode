weekend = ['sun', 'mon']
data = []
nums = [1,2,3,4]
measurements = [3.4,2.4]
Objects = ['Hello',2,False, 4.5] #inheritance in object oriented programming

condition = "Hello" not in Objects #"not in" make it "False"
print(condition)

for num in nums:
    print(num**2, end= "\t")

print()
print(nums[3])
nums[3] = 18 #"nums" index 3 assigned 18. This is not allowed in tuples because tuples are immutable

x = nums[3]
for num in nums:
    print(num, end="\t")

print ()
for i in range(0,len(nums)): # range ---> 0,1,2,3
    print(nums[i], end= "\t")

print()

#concat two lists/add two lists


num1 = [1, 2, 3]
num2 = [7,8,9]
num3 = [num1+num2]

print(num1, num2, nums)

num1.append(4) #append function adds to the existing list
num1.append(5)
num1.append(6)
print(num1, "\n")
num1.extend(num2) # extend is used to add one list to another
print(num1, "\n")
num1.extend([10,11,12])
print(num1, "\n")

'''options = ["Yes", "Y", "y", "yea"]
user_input = input("Do you want to continue? y/n\n")
if user_input in options:
    print("continue")
'''

days = ('mon', 'tue')
print(days[0])
#days[0] = 'thu' #mistake, tuples are immutable - unable to be changed
print(days)

days_ = list(days)
days_.append('wed')
print(days_)
some_days = tuple(days_)
print(some_days)

#What is iterable? sequentially accessing elements within a collection or sequence, one by one - used in a for loop


#Deleting from a list
print(num1)
del num1[3]
print(num1)
num1.pop(4) #removes by index - removed "6"
print(num1)
num1.remove(12) #remove by value
print(num1)
del num1 # deletes it from memory
# print (num1) - mistake, it has been cleared from memory
print('num3',num3)
num3.clear()
print("num3",num3)


vowels = ['a', 'e', 'i', 'o', 'u']
text = "Hello, how are you?" #string ---> iterable

