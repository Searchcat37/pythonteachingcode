# [] create Element_Quiz
import os

def get_names():
    user_elements = [] 
    print("Welcome Colin Kennel! List any 5 of the first 20 elements in the Periodic Table")

    while len(user_elements) < 5:
        element = input("Enter the name of an element: ").strip().lower()

        if element == "":
            print("You must enter a name.")
            continue
        
        if element in user_elements:
            print(f"{element.title()} was already entered")
            continue

        user_elements.append(element)

    return user_elements

os.system("curl -O https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt")
elements_file = open("elements1_20.txt", "r")

elements_20 = []

for name in elements_file:
    clean_element = name.strip().lower()
    if clean_element != "":
        elements_20.append(clean_element)


elements_file.close()

responses = get_names()

correct = []
incorrect = []

for name in responses:
    if name in elements_20:
        correct.append(name.title())
    else:
        incorrect.append(name.title())

score_percent = len(correct) * 20  # (since 5 questions each is 20%)

print()
print(f"{score_percent} % correct")

if correct:
    print("Found:", " ".join(correct))
else:
    print("Found: None")

if incorrect:
    print("Not Found:", " ".join(incorrect))
else:
    print("Not Found: None")
