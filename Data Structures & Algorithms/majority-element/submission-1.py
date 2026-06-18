class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        count = {}
        result = 0
        maxCount = 0

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
            if count[num] > maxCount:
                result = num
                maxCount = count[num]
        
        return result