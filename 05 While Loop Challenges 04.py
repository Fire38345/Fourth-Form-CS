ans = "y"
count = 0

while ans == "y":
    name = input("Enter the name of somebody you want to invite to the party")
    print(name + " has now been invited")
    count = count + 1
    ans = input("do you want to invite someone else? y/n")
print("You have invited", count , "people")
