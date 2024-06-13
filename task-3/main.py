# Check List Order
# Objective: Write a function `check` that takes a list and 
# determines whether it is strictly increasing,
# strictly decreasing, or neither.
# Parameters:
# - list: A list of integers with a minimum length of 2.
# Returns:
# - A string: "increasing" if the list is strictly increasing,
# "decreasing" if the list is strictly decreasing, or "neither" otherwise.
# Notes:
# - A list is strictly increasing if each element is
# greater than the preceding one.
# - A list is strictly decreasing if each element is less than the
# preceding one.
# - If any two consecutive elements are equal, the list is
# considered "neither".

def check(list_):
    list_len = len(list_)
    if list_ and list_len > 1:
        increasing = all([list_[i] < list_[i+1] for i in range(list_len - 1)])
        decreasing = all([list_[i] > list_[i+1] for i in range(list_len - 1)])
        if increasing:
            return "increasing"
        if decreasing:
            return "decreasing"
    return "neither"


# Examples:
print(check([1, 2, 3]))  # Expected: "increasing"
print(check([3, 2, 1]))  # Expected: "decreasing"
print(check([1, 2, 1]))  # Expected: "neither"
print(check([12, 1]))  # Expected: "neither"
