print("Task3 Coding")
a = 1234
b = 4321
c = a*b
print(a*b)
print(c)

a, b = "Hello", "World"
print(a,b)
#a is "Hello" and b is "World"

a = b = [1,2,3]
#a and b are both [1,2,3]
print("\n")

print("Task5 Coding")
a = "Never"
b = "say"
c = "\"never\""
print(a,b,c)
print()

print("        Testing")
print()
start = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye'
print(start + start + middle + end)
print("Using copy '*' syntax")
print()

print("list of Reserver Words")
first_line = ['and','exec','not','as','finally','or','assert']
second_line = ['for','pass','break','from','print','class','global']
third_line = ['raise','continue','if','return','def','import','try']
fourth_line = ['del','in','while','elif','is','with','else']
fifth_line = ['lambda','yield','except']
all_resWord = [first_line,second_line,third_line,fourth_line,fifth_line]
print (first_line,"\n",second_line,"\n",third_line,"\n",fourth_line,"\n",fifth_line)
print()

print("The difference between ")
print (repr("%r"))
print("and")
print (str("%s"))
print("Obvlously and fundamentally %r <-> repr, %s <-> str")
print("In Python, there are two builtin functions for turning an object into a string: str vs. repr")
print("str is supposed to be a friendly, human readable string. repr is supposed to include detailed information about an object's content.")
print("(sometimes, they'll return the same thing, such as for integers).")
print (repr('hi'))
print (str('hi'))
print()

print("Task6 Coding")
a = "love you"
a is "love you"
print(a is "love you")
print()

print("Task7 Coding")
def fact(j):
    sum = 0
    j = input("Input a number to calculate its factorial:")
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
        return sum
    for i in range(5):
        print('%d != %d' % (i,fact(i)))
    print()

name = input("What is your name?")
print(name,"is a good name")
print()

print("Task8 Coding")
while True:
    ccc = 0
    ccc = input("Please input a positive integer: ")
    if int(ccc) <= 0:
        print("POSITIVE INTEGER")
        continue
    else:
        for i in range(1,int(ccc)):
            if((int(ccc) % i) == 0):
                print(i)
        break
print()

print("Task9 coding")
while True:
    number = input("How many lines of a triangle you want to draw: ")
    for i in range(1,int(number) + 1):
        #for j in range(int(number),1,-1):
        print((int(number) - i) * " ", end = '')
        if(i <= 3):
            print((2 * int(i) - 1) * "*", end = '')
        if(i > 3):
            print((2 * int(i)) * "*", end = '')
        print()
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print()

print("Task10 coding")
while True:
    number = input("Please input an integer to decide whether it is a perfect square: (Please input -1 to exit.) ")
    sign, radic = 0, 0
    for i in range(1,int(number)+1):
        if(int(number) == i * i):
            radic = i
            sign = 1
        #if(int(number) == -1):
         #   sign = -1
    #if sign == -1:
     #   print("Bye bye")
      #  break
    #sign == 1 and print("Yes, it's a perfect square and its radicand is %d" % i) or print("No, it's not a perfect square.")
    print("Yes, it's a perfect square and its radicand is %d" % radic) if sign == 1 else print("No, it's not a perfect square.")
print()
