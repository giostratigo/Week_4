# Calculate and return the total weight.
def sum_weights(person_weight, inventory_weight):
    return person_weight + inventory_weight


# Use the total weight to calculate and return the average.
def calc_avg_weight(person_weight, inventory_weight):
    return sum_weights(person_weight, inventory_weight) / 2


# Get the weights and display the requested calculation.
def run():
    print("What is the weight of the person?")
    person_weight = float(input())

    print("\nWhat is the weight of their inventory?")
    inventory_weight = float(input())

    print("\nWhat would you like to calculate (sum or average)?")
    choice = input()

    if choice == "sum":
        total = sum_weights(person_weight, inventory_weight)
        print(f"\nThe sum of weights is {total:g}.")
    elif choice == "average":
        average = calc_avg_weight(person_weight, inventory_weight)
        print(f"\nThe average weight is {average:g}.")


# Run the program.
run()