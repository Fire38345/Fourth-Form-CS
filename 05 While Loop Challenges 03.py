num = int(input("Enter a number"))
total = num
ans = "y"

while ans == "y":
    num1 = int(input("Enter another number"))
    total = total + num1
    ans = input("Do you want to add another number y/n")
print(total)
