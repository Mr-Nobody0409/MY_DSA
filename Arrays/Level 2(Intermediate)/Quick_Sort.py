# ------------------------------
# Problem: Quick Sort
# Sort an array using the fast divide & conquer method.
#
# Example:
# Input:  [10, 7, 8, 9, 1, 5]
# Output: [1, 5, 7, 8, 9, 10]
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Quick Sort (O(n log n) average)
# ------------------------------

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose middle element
    left = [x for x in arr if x < pivot]      # Smaller elements
    mid = [x for x in arr if x == pivot]      # Pivot elements
    right = [x for x in arr if x > pivot]     # Larger elements

    return quick_sort(left) + mid + quick_sort(right)


arr = [10, 7, 8, 9, 1, 5]
print("Sorted Array:", quick_sort(arr))

# ---------- Output -----------
# Sorted Array: [1, 5, 7, 8, 9, 10]
