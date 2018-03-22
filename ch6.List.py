num_list = [-1,2,-4]
def absList(num_list):
    for i in len(num_list):
        if i >= 0:
            i = i
        else:
        i = 0 - i
        #i = (i > 0) and i or -i
        #i = [-i,i](i>=0)
        #num_list(i) = (num_list(i) >= 0)and num_list(i) or -num_list(i)
    # YOUR CODE HERE
absList(num_list)
print(num_list)

print("Task1 coding")
name_list = ['Mary','Tracy']
def hello(name_list):
    for name in name_list:
        print("Hello, " + name + "!")
hello(name_list)
print()
