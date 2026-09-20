class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        
        if (len(s) != len(t)): return False

        for i in range(len(s)):
            if (s[i] not in count):
                count[s[i]] = 1
            else:
                count[s[i]] += 1

        for i in range (len(s)):
            if (t.count(s[i]) != count[s[i]]): return False


        return True

        

