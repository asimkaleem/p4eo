s = "Monty Python"
slice1 = s[2:5]
print (slice1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
u = "Monty Python"
slice2 = u[0:50]
print(slice2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for letter in u:
    if letter== 'y':
        print("We have found a : ",letter)
    else:
        print ("We have found nothing.")
