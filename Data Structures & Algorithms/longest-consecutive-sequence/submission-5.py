class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        mydict ={}
        for i in range(len(nums)):
            if nums[i] in mydict.keys():
                mydict[nums[i]] = mydict[nums[i]] + 1
            else:
                mydict[nums[i]] = 1
        mylist = sorted(list(mydict.keys()))
        if len(mylist) == 0:
            return 0
        else:
            maxlength = 1
            count = 1

            myset = set(mylist)
            for j in range(len(mylist)):
                if (mylist[j]+1) in myset:
                    count = count + 1
                else:
                    if (count >= maxlength):
                        maxlength = count
                    count = 1
            return maxlength