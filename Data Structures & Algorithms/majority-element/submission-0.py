class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        counts = {}
        result = None
        highest = 0

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for count in counts:
            if counts[count] > highest:
                result = count
                highest = counts[count]
        
        return result