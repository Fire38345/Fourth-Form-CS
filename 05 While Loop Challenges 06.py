num = int(input("Enter a number between 10 and 20"))

while num < 10 or num > 20:
    if num <10:
        print("too low")
        

    elif num >20:
        print("too high")
        
    num = int(input("Try again"))

print("thank you")
