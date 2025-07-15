# we are using 2 pointer to solve this sum
class Solution(object):
    def maxProfit(self, prices):
        left = 0  #left pointer (buying price)
        right = 1 #right pointer (selling price)
        max_profit = 0 # max profit intilization

        while right < len(prices) :
            if prices[left]< prices[right]: # for it to be profitable the buying price should always be greater than selling price
                total = prices[right] - prices[left]
                max_profit = max(max_profit, total)
            else:
                left = right # if selling price is lesser than buying price we make the selling price the buying price
            right += 1        
        return max_profit
