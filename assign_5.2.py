#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        ival=int(sval)

    except:
        print('Invalid input')

    continue

if largest is None:
    largest=ival
    #print(largest,'primeiro input largest')
elif ival> largest:
 	ival=largest

if smallest is None:
    smallest=ival
    #print(smallest,'primeiro input smallest')
elif ival<smallest:
    ival=smallest
    #print(smallest,'comparado smallest')

print("Maximum is", largest)
print("Minimum is", smallest)


#
largest = None
smallest = None
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        ival=int(sval)
#        print(ival)
    except:
        print('Invalid input')
    continue
if ival>largest:
    largest=ival
else:
    ival=smallest

print("Maximum is", largest)
print("Minimum is", smallest)
