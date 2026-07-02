class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        p = 0
        buy = prices[0]        
        for i in range(1,len(prices)):
            sell = prices[i]
            buy = min(buy,sell)
            p = max(p, sell-buy)
        return p
