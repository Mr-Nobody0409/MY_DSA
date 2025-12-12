# ------------------------------
# Problem: Insertion Sort
# Sort an array by repeatedly inserting elements in their correct position.
#
# Example:
# Input:  [5, 2, 4, 6, 1, 3]
# Output: [1, 2, 3, 4, 5, 6]
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Insertion Sort (O(n²))
# ------------------------------

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [5, 2, 4, 6, 1, 3]
print("Sorted Array:", insertion_sort(arr))

# ---------- Output -----------
# Sorted Array: [1, 2, 3, 4, 5, 6]
