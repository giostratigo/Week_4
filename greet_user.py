# Define a function with no parameters.
def listen():
    # Ask the user what sound they heard.
    print("What sound did you hear?")
    sound = input()

    # Display the sound with an exclamation mark.
    print("That was a loud " + sound + "!")


# Call the function.
listen()