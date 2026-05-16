class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict.keys():
                s_dict[s[i]] += 1
            else:
               s_dict[s[i]] = 0
        for i in range(len(t)):
            if t[i] in t_dict.keys():
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 0
        
        if s_dict == t_dict:
            return True
        else:
            return False


