class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fst,snd = 0, 1
        out = set()

        for fst in range(len(nums)):
            seen = set()

            for snd in range(fst+1,len(nums)):
                if (-nums[fst]-nums[snd]) in seen:
                    out.add(tuple(sorted([nums[fst], nums[snd],(-nums[fst]-nums[snd])])))
                seen.add(nums[snd])

        return [list(x) for x in out]