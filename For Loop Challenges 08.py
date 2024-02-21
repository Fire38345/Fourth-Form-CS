people = int(input("How many people do you want to invite to the party"))

if people < 10:
    for i in range(people):
        name = input("What is their name?")
        print(name + " has been invited")
if people >= 10:
    print("Too many people")
