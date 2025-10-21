print("welcome to  the average calculation program")

continue_option = "Y"
while continue_option == "Y":
    sum = 0
    print ("Please enter any set of numbers")
    num = 0
    count = 0
    while num != -50:  #use num only if you initialize it
        count += 1
        sum += num
        num = float(input())

    count -= 1
    average = sum/count
    print("The average of the numbers you entered is:", average)
    continue_option = input("Do you wan to continue?Y/N\t")
   
print("Exit average calcuation program")
    

