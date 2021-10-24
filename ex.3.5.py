def great_line(length):
    print("|", end="")
    for el in range(length):
        print("....", end='|')
    print()
    for el in range(length + 1):
        spacing = "   "
        if el > 9:
            spacing = "  "
        print(el, spacing, end="")


great_line(10)
