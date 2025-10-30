#sets are unordered, uses {}

names = set()
names.add('john')
names.add('Jake')
print(names)

#review tuples
data = (1, 2, 3, 3)
dataset = set(data) 
print(dataset)


text = "Hello guys i think I am like programming"
unique = set(text)
print(unique)
unique.remove('g')
print(unique)

for char in unique:
    print(char, end='\t')


#Set functions

print(min(dataset))
print(max(dataset))

del dataset
dataset = {3,4,5,8}
print (dataset)


num1 = {1,2,3}
num2 = {2,3,4}

num3 = num1.intersection(num2)
num4 = num1.union(num2)
num5 = num1.difference(num2)
num6 = num2.difference(num1)

print(num3)
print(num4)
print(num5)
print(num6)

#Set methods
data1 = {1,2,3,4,5}
data2 = {0,1,5,8,9,10}
data1.update(data2)
print(data1)


