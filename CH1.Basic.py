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
print("\n")

print("        Testing")
print("\n")
start = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye'
print(start + start + middle + end)
print("Using copy '*' syntax")
print('\n')

print("list of Reserver Words")
first_line = ['and','exec','not','as','finally','or','assert']
second_line = ['for','pass','break','from','print','class','global']
third_line = ['raise','continue','if','return','def','import','try']
fourth_line = ['del','in','while','elif','is','with','else']
fifth_line = ['lambda','yield','except']
all_resWord = [first_line,second_line,third_line,fourth_line,fifth_line]
print (first_line,"\n",second_line,"\n",third_line,"\n",fourth_line,"\n",fifth_line)
print("\n")

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
print("\n")

print("Task6 Coding")
a = "love you"
a is "love you"
print(a is "love you")
print("\n")

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
    print("\n")

name = input("What is your name?")
print(name,"is a good name")
print("\n")

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
print("\n")
