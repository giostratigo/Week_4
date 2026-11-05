# Define a function with one parameter called plan.
def escape_by(plan):
    # Check the plan and display the appropriate response.
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


# Call the function with three different escape plans.
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")