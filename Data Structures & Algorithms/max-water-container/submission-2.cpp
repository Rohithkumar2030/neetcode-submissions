class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();
        int left = 0;
        int right = n-1, maxarea = 0;
        while (left<right){
            int l = min(heights[left],heights[right]);
            int b = right -left;
            maxarea =max(maxarea,l*b);
            if (heights[left] < heights[right]){
                left ++;
            }
            else right--;
        }
        return maxarea;
    }
};
