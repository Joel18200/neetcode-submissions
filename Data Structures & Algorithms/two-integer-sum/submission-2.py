class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j={}
        for i in range(len(nums)):
            sum=target-nums[i]
            if sum in j:
                return [j[sum],i]
            j[nums[i]]=i        


        