class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen={}
        left=0
        max_count=0
        result=0
        for right in range(len(s)):
            seen[s[right]]=seen.get(s[right],0)+1 
            max_count=max(max_count,seen[s[right]])
            while (right-left+1)-max_count>k:
                seen[s[left]]-=1
                left+=1
            result=max(result,right-left+1)
        return result          

        