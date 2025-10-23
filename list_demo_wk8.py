weekend = ['sun', 'mon']
data = []
nums = [1,2,3,4]
measurements = [3.4,2.4]
Objects = ['Hello',2,False, 4.5] #inheritance in object oriented programming

condition = "Hello" not in Objects
print(condition)

for num in nums:
    print(num**2, end= "\t")

print()
print(nums[3])
nums[3] = 18 #This is not allowed in tuples because tuples are immutable

x = nums[3]
for num in nums:
    print(num, end="\t")


for i in range(0,len(nums)): # range ---> 0,1,2,3
    print(nums[i], end= "\t")


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

options = ["Yes", "Y", "y"]
user_input = input("Do you want to continue? y/n\n")
if user_input in options:
    print("continue")