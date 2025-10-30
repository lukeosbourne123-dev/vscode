'''
print("Welcome to the Grade Registry Program")
run_program = True
student_name = []
student_gpa = []
loop_count = 0
while run_program:
    print("\nWould you like to add a new student? y(yes),n(no)\n")
    confirmation_input = str(input(""))
    confirmation_input = confirmation_input.lower()
    if confirmation_input == 'y' or confirmation_input == 'yes':
        loop_count+=1
        print("\nEnter the student's name:\n")
        input_name = str(input(""))
        student_name.append(input_name)
        print("\nEnter student GPA for each subject. Enter -1 to stop entering GPA\n")
        count = 0
        sum = 0.0
        while True:
            gpa_input = float(input(""))
            if gpa_input == -1:
                break
            sum+=gpa_input
            count+=1
        if count != 0:    
            average = sum/count
            student_gpa.append(average)
        else:
            student_gpa.append(0)
    elif confirmation_input == 'n' or confirmation_input == 'no':
        run_program = False
    else:
        print("\nIncorrect Input, please enter y(yes)/n(no)\n")
print("This is the list of students in the system, and their corresponding accumulative GPA")
for i in range(loop_count):
        print(student_name[i], format(student_gpa[i], ".2f"))

'''

print("Welcome to the Grade Registry Program")
student_gpa = dict()
while True:
    print("\nWould you like to add a new student? y(yes),n(no)\n")
    confirmation_input = str(input(""))
    confirmation_input = confirmation_input.lower()
    if confirmation_input == 'y' or confirmation_input == 'yes':
        print("\nEnter the student's name:\n")
        input_name = str(input(""))
        print("\nEnter student GPA for each subject. Enter -1 to stop entering GPA\n")
        gpa = []
        while True:
            gpa_input = float(input(""))
            if gpa_input == -1:
                break
            elif gpa_input > 4 or gpa_input < 0:
                print("\ninvalid input\n")
            else:
                gpa.append(gpa_input)
        if len(gpa) != 0:     
            average_gpa = sum(gpa)/len(gpa)
        else:
            average_gpa = 0
        student_gpa[input_name] = average_gpa
    elif confirmation_input == 'n' or confirmation_input == 'no':
        break
    else:
        print("\nIncorrect Input, please enter y(yes)/n(no)\n")
print("This is the list of students in the system, and their corresponding accumulative GPA")
for name,gpa in student_gpa.items():
        print(name, format(gpa, ".2f"))