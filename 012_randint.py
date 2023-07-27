##import random
##import time
###2 secind
##
##print("Dice! ")
##while True:
##    while 1:
##        value = random.randint(1, 6)
##        print("Dice value: %d" %value)
##        time.sleep(2)
##endvalue = int(input("endvalue: "))

#range
#start = 1
#end : input
#num count -> use while loop

import random
import time

print("Dice")
startvalue = int(input("startvalue: "))
print(startvalue)
while 1:
    value = random.randint(1, 6)
    print("Dice value: %d" %value)
endvalue = int(input("endvalue: "))
print(endvalue)
