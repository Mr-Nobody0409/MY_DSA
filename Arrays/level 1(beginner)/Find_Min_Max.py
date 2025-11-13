# ------------------------------
# Problem: Find Smallest and Largest Elements
# Identify the minimum and maximum values within an array.
#
# Example:
# Input:  [3, 1, 8, 5, 2]
# Output: Min = 1, Max = 8
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Using built-in min() and max() or single loop traversal (O(n))
# ------------------------------

def find_min_max(arr):
    return min(arr), max(arr)

#------------- or --------------
def find_min_max(arr):
    minimum = maximum = arr[0]
    for num in arr[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum, maximum

arr = [3, 1, 8, 5, 2]
print("Min, Max:", find_min_max(arr))

# ---------- Output -----------
# Min, Max: (1, 8)