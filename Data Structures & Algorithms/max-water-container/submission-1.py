class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        maxarea = 0
        while left < right:
            b = right-left
            l= min(height[left],height[right])
            maxarea= max(maxarea,l*b)
            if (height[left]<height[right]):
                left=left+1
            elif (height[left]>=height[right]):
                right =right -1
        return maxarea


        