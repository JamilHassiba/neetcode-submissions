class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## O(1) space solution ##

        if len(s) != len(t):
            return False

        for s_char in s:
            if not s_char in t:
                return False
            t = t.replace(s_char, "", 1)
        return True
