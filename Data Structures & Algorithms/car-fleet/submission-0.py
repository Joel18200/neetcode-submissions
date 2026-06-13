class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pair=list(zip(position,speed))
        pair.sort()
        for i in range(len(pair)-1,-1,-1):
            p,s=pair[i]
            result=(target-p)/s
            if not stack or  result>stack[-1]:
                stack.append(result)
        return len(stack)        
        