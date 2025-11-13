# ------------------------------
# Problem: Reverse an Array
# Reverse the order of elements in a given array.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Using slicing (O(n))
# ------------------------------

def reverse_array(arr):
    return arr[::-1]

# Example Run
arr = [1, 2, 3, 4, 5]
print("Reversed Array:", reverse_array(arr))

# ---------- Output -----------
# Reversed Array: [5, 4, 3, 2, 1]