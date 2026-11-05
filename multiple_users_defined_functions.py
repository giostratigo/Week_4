# Display a ladder with the specified number of steps.
def display_ladder(steps):
    print("| |")
    for step in range(steps):
        print("***")
        print("| |")


# Ask the user for the number of steps and display the ladder.
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    print()
    display_ladder(steps)


# Call the function to start the program.
create_ladder()