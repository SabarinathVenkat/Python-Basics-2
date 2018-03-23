import sys

def digit(num):
    if num <= 9:
        return num
    else:
        return digit(reduce(lambda x,y:int(x)+int(y),str(num)))
def print_line():
    print
    print "-" * 20

# Let us explore for, while, if,

# Let us create a empty if block just for fun:

if (1==1):
    pass

# Now with an Empty else part
if (len("ThisIsSomeString") > 10):
    print "Its a long string!!"
else:
    pass

print_line()

a = input("Enter Something:")

if isinstance(a,int):
    print "You have entered a number, lets analyze it"
    print "it sums upto %d"%(digit(a))
elif isinstance(a,str):
    print "The reverse of the string is ","".join(reversed(a))
else:
    print "Not sure what this is..", a
print_line()

###### For Loops

# Basic for loops
for i in "Hi":
    print ord(i),
print_line()

for i in range(3):
    print(i),


print_line()

# For loop with else
for i in range(3):
    pass
else:
    print "Exhausted the loop"
print_line()

for i in range(4):
    if i == 3:
        break
else:
    print "This will never print"
print "Exhaused the loop 2"


i=0
while(i<3):
    print i,
    i+=1

for i in range(20):
    if i % 2 ==0:
        continue
    else:
        print i,
