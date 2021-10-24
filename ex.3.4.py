def get_input():
    while True:
        x = input("Enter value: ")
        if x == 'stop':
            break
        elif x.isnumeric():
            print("Result:(", x, ",", pow(float(x), 3), ")")
        else:
            print("Got an error")


get_input()
