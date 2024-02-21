total = 0

for i in range(5):
    num = int(input("Enter a number"))
    ans = input("Do you want that number added? y/n")
    if ans == "y":
        total = total + num

print(total)
