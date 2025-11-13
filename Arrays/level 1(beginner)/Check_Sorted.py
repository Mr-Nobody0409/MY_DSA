# ------------------------------
# Problem: Check if Array is Sorted
# Determine if a given array is sorted in ascending order.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: True
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Compare consecutive elements (O(n))
# ------------------------------

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = [1, 2, 3, 4, 5]
print("Is sorted:", is_sorted(arr))

# ---------- Output -----------
# Is sorted: True