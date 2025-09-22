# Create name check code

# [ ] get input for input_test variable
input_test = input("Enter Names:")
# [ ] print "True" message if "John" is in the input or False message if not
for name in input_test.split():
    if name == "John":
        print("John found = True")
    else:
        print("John found = False")
# [ ] print True message if your name is in the input or False if not
for name in input_test.split():
    if name == "Colin":
        print("Colin found = True")
    else:
        print("Colin found = False")

# [ ] Challenge: Check if another person's name is in the input - print message
for name in input_test.split():
    if name == "Colin":
        print("Colin found = True")
    elif name == "Kell":
        print("Kell found = True")
    else:
        print("Colin or Kell found = False")
# [ ] Challenge: make your code work for input regardless of case, e.g. - print True for "mary", "Mary", "MARY" or "MaRy"  
input_test_lower = input_test.lower()
for name in input_test_lower.split():
    if name == "john":
        print("john =", name, ": True")
    else:
        print("john =", name, ": False")
# [ ] Challenge: Check if a fourth person's name is in the input - print message
if len(input_test) >= 4:
    print(input_test[5])
else:
    print("Not long enough")
    
