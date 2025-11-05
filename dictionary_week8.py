student_data = {"Sam":3.4, "John":3.2} #the pair of key values can be of any type

info = {1:'Sam', 2:'Sam', 3:'Max', 3:'Sara'}

print(student_data)
print(info)

students_gpa = dict()
print(students_gpa)

nums = [1,2,3,4]
nums2 = (1,2,3,4)

print(nums[1])
print(nums2[-1])
print("Sam:", student_data["Sam"])

print(student_data.keys())
print(student_data.values())

avg_temp = {1:28.3,2:23.4,3:25.2,4:40.3,5:3.3,6:26.4,7:23.6}
print(avg_temp)
print(avg_temp.keys())
print(avg_temp.values())
print(avg_temp[3])
print()

for day in avg_temp:
    print(day, avg_temp[day])
print()
for day, temp in avg_temp.items():
    print(day, temp)
print()
avg_temp[8] = 3.4 #added 3.4 at index 8

print(len(avg_temp))
print("max", max(avg_temp))
print("min", min(avg_temp))

avg_temp2 = {4:24.5, 1:31, 9:23}
avg_temp.update(avg_temp2)

for day, temp in avg_temp.items():
    print(day, temp)
print()
avg_temp.pop(5)
avg_temp.pop(8)
for day, temp in avg_temp.items():
    print(day, temp)

avg_temp.clear()
print(avg_temp)