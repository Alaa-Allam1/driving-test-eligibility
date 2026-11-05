age = int(input("Enter your age \n"))

if age >= 18:
    print("Oh! You can drive")
    license = input("Do you have a license? (Yes) or (No) \n").lower()
    if license == "yes":
        print("Good. you can do it")
    else:
        print("Sorry. you can't do it")
else:
    print("You can't drive")
        