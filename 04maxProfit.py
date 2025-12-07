def maxProfit(prices):
    profit = 0
    min_price = prices[0]
    for currentPriceIndex in range(1, len(prices)):
        profit = max(profit, prices[currentPriceIndex] - min_price)
        min_price = min(prices[currentPriceIndex], min_price)
    return profit
    

s = [int(x) for x in input().split()]
print(maxProfit(s))
