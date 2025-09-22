# [ ] create, call and test fishstore() function 
name = "Colin Kennel."

# define the function
def fishstore(fish, price):
    return "Fish Type: " + fish + " costs $" + price

# gather input from user
fish_entry = input("Enter the type of fish: ")
price_entry = input("Enter the price of the fish: ")

# call the function
report = fishstore(fish_entry, price_entry)

# print the result with your full name
print("Report for,",name,report)
