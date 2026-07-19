lass Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:

        # If current range is sorted, first element is minimum
           if nums[low] < nums[high]:
              return nums[low]

           mid = low + (high - low) // 2

        # Minimum lies in right half
           if nums[mid] > nums[high]:
              low = mid + 1
        # Minimum lies in left half (including mid)
           else:
              high = mid

    # low == high points to the minimum element
        return nums[low]
