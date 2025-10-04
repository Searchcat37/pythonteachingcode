def adding_report(report="T"):
    total = 0
    items = ""
    print('Input an integer to add to the total or "Q" to quit')
    while True:
        entry = input('Enter an integer or "Q": ')
        if entry.isdigit():
            total += int(entry)
            if report == "A":
                items += entry + "\n"
        elif entry.lower().startswith("q"):
            if report == "A":
                print("\nItems")
                print(items)
            print("Total:")
            print(total)
            print("Calculated by: Colin Kennel")
            break
        else:
            print(entry, "is invalid input")

adding_report("A")
adding_report("T")