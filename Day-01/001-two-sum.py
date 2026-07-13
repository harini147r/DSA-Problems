"""
LeetCode #1 - Two Sum
Platforms: LeetCode, GeeksforGeeks ("Two Sum – Pair with Given Sum")
Topic: Arrays & Hashing
Difficulty: Easy

Problem:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Returns indices [i, j] such that nums[i] + nums[j] == target.
    Assumes exactly one solution exists and you cannot use the same element twice.
    """
    seen = {}  # number -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    # According to problem statement, this line is never reached
    return []


# usage (for local testing)
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1]