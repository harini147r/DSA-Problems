class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            # If current is negative, swap because signs will flip
            if current < 0:
                max_product, min_product = min_product, max_product

            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)

            result = max(result, max_product)

        return result
        
        