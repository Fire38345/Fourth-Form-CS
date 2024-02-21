ans = input("Do you want to count up or down? u/d")

if ans == "u":
    top = int(input("Enter the top number"))
    for i in range(1,top+1):
        print(i)
elif ans == "d":
    bottom = int(input("Enter a number below 20"))
    for i in range(20, bottom-1, -1):
        print(i)
else:
    print("I don't understand")
                       
