class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i, num in enumerate(nums):
            if num in differences:
                j = differences[num]
                return [j, i]

            diff: int = target - num

            differences[diff] = i
        
        return []