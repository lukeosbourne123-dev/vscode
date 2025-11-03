print ("Welcome to Showers of Blessings Apostolic Church Registry")

members_info = dict()
names = []


while True:
    print("Would you like to be added to SBAC's registry? y(yes) n(no) \n")
    confirm = str(input ("")) 
    confirm = confirm.lower()
    if confirm == "y" or confirm == "yes":

        print ("Please enter your name. \n")
        given_name = str(input(""))
        names.append(given_name)
    elif confirm == "n" or confirm == "y":
        break
    print ("Thank you for visiting, hope to see you again")
for char in names:
     print("Congrats:", given_name, "You are now a member of SBAC Apostolic")
        
