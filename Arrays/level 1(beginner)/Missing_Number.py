# ------------------------------
# Problem: Find Missing Number
# Identify the missing number in a sequence from 1 to n.
#
# Example:
# Input:  [1, 2, 4, 5, 6]
# Output: 3
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Sum formula (O(n))
# ------------------------------

def missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)

arr = [1, 2, 4, 5, 6]
print("Missing number:", missing_number(arr))

# ---------- Output -----------
# Missing number: 3