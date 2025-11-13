# ------------------------------
# Problem: Rotate an Array
# Shift elements of an array by k positions to the right.
#
# Example:
# Input:  [1, 2, 3, 4, 5, 6, 7], k = 2
# Output: [6, 7, 1, 2, 3, 4, 5]
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Slicing and Modulo (O(n))
# ------------------------------

def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
print("Rotated Array:", rotate_array(arr, k))
