ans = str(input("Is it raining?")).lower()


if ans == "yes":
    other = str(input("Is it windy?"))
    if other == "yes":
        print("it is too windy for an umbrella")
    else:
        print("take an umbrella")
else:
    print("Enjoy your day")
