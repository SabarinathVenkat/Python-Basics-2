"""
This is a Python script to explore user input options
"""

# You can get user input using either of these commands raw_input, input
# raw_input accepts all user inputs as strings


a = raw_input("Enter a number:")
b = raw_input("Enter another number:")

print "\nLet's see if we can add these to numbers"
print "a+b = ",a+b

print "\n Lets try converting it to integer and add"
print "int(a)+int(b) = ", int(a)+int(b)

# Let's try input , input tries to map the user input data to correct data types
c = ''
while (c != 42):
    c = input("Enter Something ( type 42 if you are tired ):")
    print "You have entered a ", type(c)

