# ------------------------------
# Problem: Merge Sort
# Efficiently sort an array using divide & conquer.
#
# Example:
# Input:  [38, 27, 43, 3, 9, 82, 10]
# Output: [3, 9, 10, 27, 38, 43, 82]
# ------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Merge Sort (O(n log n))
# ------------------------------

def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive sorting
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge both halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted Array:", merge_sort(arr))

# ---------- Output -----------
# Sorted Array: [3, 9, 10, 27, 38, 43, 82]
