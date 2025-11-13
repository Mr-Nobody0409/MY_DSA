# ------------------------------
# Problem: Two Sum
# Given an array nums of integers and an integer target, return the indices of the two numbers such that they add up to target.
# Assume exactly one valid solution exists, and the same element cannot be used twice.

# Example:
# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9
#-------------------------------
# Author : Lohith Reddy Bodumallu
# Language : Python
# Approach : Hash Map (O(n))
# ------------------------------

def two_sum(nums, target):
    """
    Return indices of the two numbers such that they add up to target.
    """
    index_map = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i

    # If no solution is found (though problem guarantees one)
    return []

# Example Run
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("Indices:", result)        # Output: [0, 1]
    print("Values:", [nums[i] for i in result])
    
# -----------OUTPUT-----------
# Indices: [0, 1]
# Values: [2, 7]
    
    
    
    
