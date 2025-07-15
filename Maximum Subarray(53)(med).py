class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0] #intilize max sum variable
        current_sum = 0 

        for n in nums:
            if current_sum < 0: # if current_sum is in negatives reset it to zero cause we need max sum
                current_sum = 0
            current_sum += n # add the values
            max_sum = max(max_sum, current_sum)   # comapiring and getting the max sum

        return max_sum
