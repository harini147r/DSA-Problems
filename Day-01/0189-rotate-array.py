class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        # Reverse helper function
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)      # Reverse the whole array
        reverse(0, k - 1)      # Reverse the first k elements
        reverse(k, n - 1)      # Reverse the remaining elements