class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=''.join(ch for ch in s.lower() if ch.isalnum() )
        f=result[::-1]
        if result==f:
            return True
        else:
            return False    