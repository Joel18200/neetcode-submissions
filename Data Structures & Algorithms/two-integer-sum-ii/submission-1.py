class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            offset=target-numbers[i]
            if offset in seen:
                return [seen[offset]+1,i+1]
            seen[numbers[i]]=i 
        