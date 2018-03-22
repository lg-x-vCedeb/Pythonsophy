my_set = {}
print("blank set: ",my_set)

my_set = {1,2.2,"hello",(1,2.3)}
print(my_set)

#set do not have duplicates, so repeated items will ber ignored
my_set = {1,2,3,4,3,4}
print(my_set)
print()

#TypeError: unhashable type: 'list'
try:
    my_set  = {1,2,[3,4]}
except TypeError:
    print(str("my_set = {1,2,[3,4]}"))
    print("TypeError: unhashable type: 'list'")
finally:
    my_set = {1,2,3,4}
print(my_set)
print()


# a tuple is defined by ()
# a list is defined by []
# a set is defined by {}
# the following set is created from a list
my_list = [1,2,3]
my_set = set(my_list)
print(my_set)

try:
    my_set[0]
except TypeError:
    print(str("my_set[0]"))
    print("TypeError: 'set' object does not support indexing")
finally:
    my_set = {3,1}
    print(my_set)
    my_set.add(2)
    print(my_set)
    my_set.add(2)
    print(my_set)
    my_set.update([2,3,4,5],[7,8])
    print(my_set)


my_set = {1,2,3,4,5,6,7,8}
try:
    my_set.discard(4)
except KeyError:
    print("KeyError: 4")
finally:
    print(my_set)

#my_set = [1,2,3,4,5,6,7,8]
#try:
#    my_set.remove(9)
#except KeyError:
#    print("KeyError: 9")
#finally:
#    print(my_set)
