#demo for positional
def get_age(name, yob):
    print("Welcome", name)
    age = 2025-yob
    print("Your age is", age)


get_age("Tom", 2000)

#Keyword args
get_age(yob=2003, name="Tom")


#print(sep=", ", "Hello","World", end="") incorrect


#default / optional arguments
print()
def pow(x,y=2):
    print(x**y)
pow(2,3)
pow(3,2)

pow(4)
pow(5)
print()

def write_settings(file="settings.config"):
    fid = open(file, 'w')
    fid.write("screensize: 1800 2800")
    fid.close()

write_settings()


def my_sum(*nums):
    sum = 0
    for num in nums:
        sum+=num
    print(sum)
    return sum
my_sum()
my_sum(4)
my_sum(4,18,20,52)
print()
#Variable length ketyword args

def print_info(**kwargs):
    for k, v in kwargs.items():
        print(k,v)

print_info(name="John", age=20, gpa=3.4)
print_info(Make="Honda", year=2000, price=3000)


