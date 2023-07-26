from datetime import date
today = date.today()

birthyear =  int(input("Your birthyear? "))
age = today.year - birthyear

if age >=15 and age<20:
    print("teenager..")
else:
    print("adult..")
print("Your age: %d" %age)
