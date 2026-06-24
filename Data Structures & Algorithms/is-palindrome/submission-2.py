import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        new = ''.join(s.split(' ')).lower()
        match = re.findall(r"[A-Z]*[a-z]*[\d]*",new)
        if match:
            final = ''
            for i in match:
                final= final+i
            if final == final[::-1]:
                return True
            else:
                return False
        else:
            return False