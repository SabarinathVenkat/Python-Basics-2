## Script Name - titanic_registry.py
## Optional Input - file
# TODO: Convert Script to use functions
# TODO: Log ( write to a file ) every print message used in the program
# TODO: Get the column that user want to Select and do analysis on them
# Let's open the file in read mode:

import sys



filename = sys.argv[1]
print "You have selected the file: %s" % (filename)

name = raw_input("What is you name? ")
age = input("What is your age?")
print type(name), type(age)

if filename == "":
    print "We need data, exiting."
    exit()

print "Starting your voyage"

f = open('./data/' + filename, 'r')
headers = f.readline().replace('"', '').strip('\n').split(',')
headers[0] = 'Id'
print headers

rows = []
for row in f:
    con = zip(headers, row.replace('"', '').strip('\n').split(','))
    rows.append(dict(con))

print rows[:3]

for row in rows:
    if None in row.values() or "" in row.values():
        print "Nulls are there!!"
        break
else:
    print "The data is clean, no Nulls"