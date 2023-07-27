##startvalue = int(input("startvalue: "))
##endvalue = int(input("endvalue: "))
##
##while startvalue <= endvalue:
##    print("Count: %d" %startvalue)
##    startvalue += 1



#use for loop

##startvalue = int(input("startvalue: "))
##endvalue = int(input("endvalue: "))
##
##for startvalue in range(startvalue, endvalue+1, 1):
##    print("Count: %d" %startvalue)

#ex
##import sys
##startvalue = int(input("startvalue: "))
##endvalue = int(input("endvalue: "))
##SUM = 0
##
##while startvalue <= endvalue:
##    #print("Count: %d" %startvalue)
##    SUM += startvalue
##    startvalue += 1
##print("sum = ", SUM)

##a = [1, 2, 3, 4, 5, 6]
##for i in a:
##    if i>3:
##        break
##    print(i)



import sys
startvalue = int(input("startvalue: "))
endvalue = int(input("endvalue: "))
SUM = 0

if (endvalue >= startvalue):
    while startvalue <= endvalue:
        print("Count: %d" %startvalue)
        SUM += startvalue
        startvalue += 1
else:
    sys.exit()
print("System exit")
print(SUM)

    


