# [] create list-o-matic as a function and call it
# [] be sure to include your spelled-out name in the welcome prompt
# [] you are welcome to use any list you like for list-o-matic, does not have to be animals 

def list_o_matic(item, list):
    if item == "":
        removed = list.pop()
        return (f"{removed} popped from list")
    elif item in list:
        list.remove(item)
        return (f"1 instance of {item} removed from list")
    else:
        list.append(item)
        return (f"1 instance of {item} appended to list")


my_list = ['cat', 'bunny', 'turtle']

print("Welcome, Colin Kennel. Look at all the animals", my_list)

while True:
    item = input("Enter the name of an animal: ")

    if item.lower() == "quit":
        print("Goodbye!")
        break

    message = list_o_matic(item, my_list)
    print(message)

    if len(my_list) == 0:
        print("List empty, goodbye!")
        break

