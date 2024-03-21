while True:
    x, y, z = input("Calculate here: " ).split()

    converted_x = int(x)
    converted_z = int(z)

    if y == "x":
        print(converted_x * converted_z)
    elif y == "/":
        print(converted_x / converted_z)
    elif y == "+":
        print(converted_x + converted_z)
    elif y== "-":
        print(converted_x - converted_z)
    else:
        print("Undefined")

