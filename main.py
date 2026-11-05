print("Program Started")

letter = input("Please enter a standard character: ")

if len(letter) == 1:

    ascii_value = ord(letter)

    print(f"The ASCII code for {letter} is: {ascii_value}")
else:
    print("Error: Please enter exactly a single character")

    print("Program Ended!")

