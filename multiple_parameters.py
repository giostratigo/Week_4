# Define a function with parameters for steps remaining and steps crossed.
def climb_ladder(steps_remaining, steps_crossed):
    # Compare the number of steps remaining with the number crossed.
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


# Call the function with two different sets of values.
climb_ladder(5, 2)
climb_ladder(2, 5)