print("Task1 Coding")
print("Write the Python code which reads in three numbers\
    from input and displays the greatest value.")
num1, num2, num3 = int(input("Please input 3 numbers:\n")),int(input()),int(input())
bigger = (num1 > num2)and ((num1 > num3)and num1 or num3) or ((num2 > num3) and num2 or num3)
print("The greatest one is %d" % bigger)
print()

print("Task2 Coding")
x, y = int(input("Please input the coordinate of point:\n")),int(input())
if x > 0 and y > 0:
    print("point(%d,%d) is in quadrant I." % (x, y))
elif x < 0 and y > 0:
    print("point(%d,%d) is in quadrant II." % (x, y))
elif x < 0 and y < 0:
    print("point(%d,%d) is in quadrant III." % (x, y))
elif x > 0 and y < 0:
    print("point(%d,%d) is in quadrant IV." % (x, y))
elif x == 0:
    if y > 0:
        print("point(%d,%d) is on the y+." % (x, y))
    elif y < 0:
        print("point(%d,%d) is on the y-." % (x, y))
    else:
        print("point(%d,%d) is the origin." % (x, y))
elif y == 0:
    if x > 0:
        print("point(%d,%d) is on the x+." % (x, y))
    elif x < 0:
        print("point(%d,%d) is on the x-." % (x, y))
    else:
        print("point(%d,%d) is the origin." % (x, y))
print()

print("Task3 Coding")
year = int(input("Please input a year number:\n"))
if year % 4 == 0:
    print("%s" % ((year % 100 != 0) and str(year) + " is a leap year" or ((year % 400 == 0) and str(year) + " is a leap year" or str(year) + " is not a leap year")))
else:
    print("%d is not a leap year" % year)
print()

print("Task4 coding")
print("Calculate the sum between 1 and 100.")
sum = 0
for i in range(1,101):
    sum += i
print("1 + 2 + 3 + ... + 99 + 100 = %d" % sum)
print()

print("Task5 coding")
print("Calculate the sum of all odd numbers between 1 and 100.")
sum = 0
odd_num = set()
for i in range(1,101):
    if i % 2:
        sum += i
        print(i,end = ' + ')
print(end = ' = ')
print(sum)
print()

print("Task6 coding")
print("The prime numbers between 2 and 19 are ",end = '')
for i in range(2,20):
    sign = 0
    for j in range(2,i):
        if i % j == 0:
            sign = 1
    if sign == 0:
        print("%d " % i,end = '')
print()

print("Task7 coding")
print("Print all the prime numbers in the following list: [32, 41, 23, 33, 18, 29, 7, 14, 76, 37, 21]")
list =  [32, 41, 23, 33, 18, 29, 7, 14, 76, 37, 21]
for i in list:
    sign = 0
    for j in range(2,i):
        if i % j == 0:
            sign = 1
    if sign == 0:
        print("%d " % i,end = '')
print()
