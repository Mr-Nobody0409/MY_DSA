# ------------------------------
# Problem: Remove Duplicates from Sorted Array
# Eliminate duplicate elements from a sorted array.
#
# Example:
# Input:  [1, 1, 2, 2, 3, 4, 4]
# Output: [1, 2, 3, 4]
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : One-pass iteration (O(n))
# ------------------------------

def remove_duplicates(arr):
    if not arr:
        return []
    result = [arr[0]]
    for num in arr[1:]:
        if num != result[-1]:
            result.append(num)
    return result

arr = [1, 1, 2, 2, 3, 4, 4]
print("Array without duplicates:", remove_duplicates(arr))
