#len
nums = [1,2,3,4,5,5,6,7,7,7,7,7,7]
n = len(nums)
print(len(nums)) #print the the total amount of variables in the list

#count function - counts the amount of a variable in a list
print(nums.count(7))

#List function converts datastructures into a list

numbers = list(range(11))

T = (1,2,3,4,5,6) # a tuple stays constant
L= list(T)

for n in numbers:
    print(n,end="\t")

for t in T:
    print(t, end="\t")

for l in L:
    print(l, end="\t")


#pop, remove and del
# 'remove' removes with value


print()
print(nums)
nums.remove(4)
print(nums)
del nums[4] 
print(nums)
