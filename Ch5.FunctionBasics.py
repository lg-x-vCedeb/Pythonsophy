print ("The syntax of function is:")
print ("def function_name(parameters)")
print ("   \"\"\"docstring\"\"\"")
print ("   statement(s)")


# function greet(name) returns a greeting message to name
def greet(name):
    """This function returns a
    greeting message to the person
     passed in as parameter"""
    return "Hello, " + name + ". Nice to meet you!"

# function greet(name) is called
msg = greet(input("What is your name? "))
print(msg)
print(great.__doc__)
print()

print("Task1 coding")
def absv(num):
    """In the code cell below, complete the function absv
    which returns the absolute value of num."""
    print("absv(%d)==%d" % (num,(num < 0) and -num or num))
absv(int(input("Please input an integer:\n")))
print()

print("Task2 coding")
def gcd(x, y):
    """ In the code cell below, complete the function gcd
    which returns the greatest common divisor (GCD) of two natural numbers x and y."""
    bigger = x if x > y else y
    for i in range(1,bigger + 1):
        if x % i == 0 and y % i == 0:
            a = i
    print("gcd(%d,%d) == %d" % (x,y,a))
gcd(int(input("Please inout two natural numbers:\n")),int(input()))
print()

print("Task3 coding")
import re
def checkPasswd(passwd):
    """In the code cell below, complete the function checkPasswd
    which checks whether the string passwd is a valid password or not. A password is valid if
    It contains no less than 8 characters
    It contains at least 1 number, 1 lower-case letter and 1 upper-case letter
    The function returns True if the passwd is valid and False otherwise.
    For example, checkPasswd('aA12331222') returns True while checkPasswd('bbb1212121') returns False."""
    # YOUR CODE HERE
    #while(1):
    code = passwd
        #if len(code) < 8:
        #    print("The code is too short.")
        #   continue
        #else:
    digit = re.compile(r'\d+')
    lowercase = re.compile(r'[a-z]+')
    uppercase = re.compile(r'[A-Z]+')
    hasDigit = digit.search(code)
    hasLower = lowercase.search(code)
    hasUpper = uppercase.search(code)
    print("checkPasswd('%s') == %s" % (code,(hasDigit and hasLower and hasUpper) and True or False))

checkPasswd(str(input("Please input your code:\n")))   
            #for i in code:
print()
