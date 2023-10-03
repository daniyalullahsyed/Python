#Problem 1

def calculate_boost_distance(speed, time):
# Calculating the boost distance
    boost_distance = speed * time
    return boost_distance

#Problem 2
def generate_silly_name():
#User's name as input
    user_name = input("Enter your name: ")

#Number of times to repeat the name as input
    repeat_count = int(input("Enter a non-negative whole number: "))

#Generate the silly name
    silly_name = user_name * repeat_count

    return silly_name

#Problem 3
print("Problem 3 Output\n")
def generate_first_track():
# Loop from 6 to 21 with a step of 3
    for i in range(6, 22, 3):
        print(i, end=" ")
        print()

# Loop from 4 to 4 with a step of 4
    for i in range(4, 5, 4):
        print(i, end=" ")
        print()
    
# Loop from 7 to 21 with a step of 7
    for i in range(7, 22, 7):
        print(i, end=" ")
        print()

# Loop from 49 to 13 with a step of -9
    for i in range(49, 12, -9):
        print(i, end=" ")
        print()
    
# Call the function to print the track components
generate_first_track()

#Problem 4
print("\nProblem 4 Output\n")
def remove_from_pool(powerups):

# Get power-up to remove
    item_to_remove = input("Enter an item to remove: ").lower()

# new list without the specified power-up (case-insensitive)
    new_powerups = [pu for pu in powerups if pu.lower() != item_to_remove]

# Print the updated pool
    for pu in new_powerups:
        print(pu)

# Sample usage
    powerup_pool_1 = ["Blue Shell", "lightning", "GREEN SHELL"]
    remove_from_pool(powerup_pool_1)

    powerup_pool_2 = ["red mushrooms", "Red MUsHrooms", "Gold Mushroom", "BaNaNa Peel"]
    remove_from_pool(powerup_pool_2)

#Problem 5
print("\nProblem 5 Output\n")
def select_powerup(index, powerups):
    if -len(powerups) <= index < len(powerups):
        selected_powerup = powerups[index]
        print(selected_powerup)

# Sample usage
select_powerup(0, ["Green Shell", "Blue Shell", "Banana Peel"])
select_powerup(-2, ["Green Shell", "Blue Shell", "Banana Peel"])
select_powerup(-4, ["Green Shell", "Blue Shell", "Banana Peel"])
select_powerup(3, ["Green Shell", "Blue Shell", "Banana Peel"])
