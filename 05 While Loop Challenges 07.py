num = 10

while num > 0:
    print("""There are""", num, """green bottles hanging on the wall,
"""
, num, """green bottles hanging on the wall,
And if one green bottle should accidentally fall""")
    num = num - 1
    ans = int(input("How many green bottles will be hanging on the wall?"))

    while ans != num:
        ans = int(input("No, try again"))
    print("They'll be", num, "green bottles hanging on the wall.")

print("They'll be no green bottles hanging on the wall.")
        

