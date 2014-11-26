__author__ = 'asim'
# Exercise 6.1 Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards.
#-----------------------------------------------------------------------------------------------------------------------
myString = "Banana The fruit"
print len(myString)

print myString[-1]
index = 0
while index > 0:
    print myString[len(myString)]
    index = index-1
print "done"









#-----------------------------------------------------------------------------------------------------------------------