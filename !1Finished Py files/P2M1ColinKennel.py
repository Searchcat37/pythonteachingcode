# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# Sample quote: "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
word = ""

quote = input("Welcome, Colin Kennel. Enter a 1 sentence quote, non-alpha separate words: ")

for char in quote:
    if char.isalpha():
        word += char
    else:
        if word != "" and word[0].lower() >= "h":
            print(word.upper())
        word = ""

if word != "" and word[0].lower() >= "h":
    print(word.upper())
