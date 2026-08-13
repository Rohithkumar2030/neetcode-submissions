class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        myset = set(nums)
        maxlen = 0
        for num in myset:
            if num -1 not in myset:
                count = 1
                next_num = num+1
                while next_num in myset:
                    count = count +1
                    next_num = next_num+1
                if count > maxlen:
                    maxlen = count
        return maxlen
