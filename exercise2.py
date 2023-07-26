import sys

num = int(input("number: "))
print(num)

if num <= 0:
    print("This is Negative num..")
    print("Program exit.")
    sys.exit()
else:
    if num % 2 == 0:
        print("Even..")
    else:
        print("Odd..")
