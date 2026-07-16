class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        answer = []

        for num in nums:
            if num in seen:
                answer.append(num)
            else:
                seen.add(num)

        return answer  