class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for price in prices:
            if price > lowest and price - lowest > max_profit:
                max_profit = price - lowest
            if price < lowest:
                lowest = price

        return max_profit
        