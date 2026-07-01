class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j={}
        for i in range(len(nums)):
            miss=target-nums[i]
            if miss in j:
                return [j[miss],i]
            j[nums[i]]=i    
        