# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  


def word_mixer(word_list):
    if len(word_list) <= 5:
        return word_list

    word_list.sort()

    new_list = []

    while len(word_list) > 3:
        new_list.append(word_list.pop(0))
        new_list.append(word_list.pop(-1))
        new_list.append(word_list.pop(-1))

    for word in word_list:
        new_list.append(word)

    return new_list


def main():
    poem = input("Welcome Colin Kennel! Enter a saying or poem: ")

    words = poem.split()

    for i in range(len(words)):
        if len(words[i]) <= 3:
            words[i] = words[i].lower()
        elif len(words[i]) >= 7:
            words[i] = words[i].upper()

    mixed = word_mixer(words)

    print(" ".join(mixed))


main()