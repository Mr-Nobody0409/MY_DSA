# ------------------------------
# Problem: Count Occurrences of a Specific Element
# Count how many times a target element appears in the array.
#
# Example:
# Input:  arr = [1, 2, 3, 2, 2, 4], target = 2
# Output: 3
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Simple counting (O(n))
# ------------------------------

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

arr = [1, 2, 3, 2, 2, 4]
target = 2
print(f"{target} appears {count_occurrences(arr, target)} times")

# ---------- Output -----------
# 2 appears 3 times