# ------------------------------
# Problem: Selection Sort
# Sort an array by repeatedly selecting the minimum element.
#
# Example:
# Input:  [64, 25, 12, 22, 11]
# Output: [11, 12, 22, 25, 64]
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Selection Sort (O(n²))
# ------------------------------

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print("Sorted Array:", selection_sort(arr))

# ---------- Output -----------
# Sorted Array: [11, 12, 22, 25, 64]
