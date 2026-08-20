class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()

        for fst in range(len(nums)):
            seen = set()

            for snd in range(fst+1,len(nums)):
                if (-nums[fst]-nums[snd]) in seen:
                    out.add(tuple(sorted([nums[fst], nums[snd],(-nums[fst]-nums[snd])])))
                seen.add(nums[snd])

        return [list(x) for x in out]

    # nums = [-1,0,1,2,-1,-4]
    # create empty set to store output triplets O(1) lookup
    # fst at -1:
    #   create empty set to store seen elements O(1) lookup
    #   snd 0 to -4:
    #       if (-nums @ fst - nums @ snd) is in seen:
    #           created a sorted tuple of nums[fst], nums[snd],(-nums[fst]-nums[snd]) and add it to out
    #   return out elements as list



    # set can't contain lists they contain only hashable objects like tuples or sets