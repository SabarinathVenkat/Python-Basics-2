def print_line():
    print
    print "-" * 20



# A simple List
a_list = [1,2,4]
print a_list[0] # The index starts with a 0
print len(a_list)

for i in a_list:
    print i**2,
print_line()
# List operaations

a_list.append(153)
print a_list

a_list.reverse()
print a_list
a_list.extend([999,998])
print a_list
print a_list.index(998)
# List Comprehension
print [x**2 for x in a_list]
print_line()


# Careful when copying lists:

list1 = [1,2,4,5]
list2 = list1
print list1
print list2
print "See what happens with shallow copy"
list1.append(8)
print list2
print_line()
# Selecting a random element from the list
from random import choice
print "A Random element from the list :",choice(a_list)
print_line()


mixed_list = [1,'a',2,3.9,3+8j]
nested_list = [1,[2,3],(2,3),2,"akd"]
# Accessing a nested list element
print nested_list[0], nested_list[1],nested_list[1][0]
print "akd" in nested_list
print 3 in nested_list

## Exercise -- Figure out how to flatten a nested list , write a function
print_line()
## Tuples and Sets
## Tuples are immutable

tup = (1,2,3)
# a tuple can have duplicates
tup = (1,1,1,2,3,'a','b','b')
print tup

print_line()
# Set are mutable , but only allows unique elements
a_set = {1,2,3}
a_set.add(13)
print a_set
a_set.add(1)
print a_set

another_set = {1,1,1,1,1,2,3,4,6,6,6,6}
print "another_set:",another_set

print_line()
# Dictionaries
a_dict = {'key1':'val1','key2':123,'list':[1,2,3],'dict':{'a':1}}
print a_dict.keys()
print a_dict.items()

# Looping through a Dictionary iterates through keys

for key in a_dict:
    print key , a_dict[key]

for key,value in a_dict.items():
    print key, type(value)

