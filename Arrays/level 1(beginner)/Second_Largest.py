# ------------------------------
# Problem: Find Second Largest Element
# Find the second largest distinct element in an array.
#
# Example:
# Input:  [10, 5, 20, 8]
# Output: 10
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Single pass with two variables (O(n))
# ------------------------------

def second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

arr = [10, 5, 20, 8]
print("Second Largest:", second_largest(arr))

# ---------- Output -----------
# Second Largest: 10