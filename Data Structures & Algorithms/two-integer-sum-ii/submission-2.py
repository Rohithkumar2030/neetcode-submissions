class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, second = 0, 1
        for first in range(len(numbers)):
            for second in range(first+1,len(numbers)):
                if numbers[first] + numbers[second] == target:
                    return [first+1, second+1]
                    break
                else:
                    continue
