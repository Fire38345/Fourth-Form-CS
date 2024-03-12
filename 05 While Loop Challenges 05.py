compnum = 50
num = int(input("Enter a number"))
count = 1

while num != compnum:
    if num > compnum:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    count += 1
    num = int(input("Enter a new guess"))
print("Well done, you took", count , "attempts")
