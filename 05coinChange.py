import sys


def coinChange(coins, amount):
    dp = []
    for i in range(0, amount + 1):
        dp.append(sys.maxsize)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if (coin <= i):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == sys.maxsize:
        return -1
    return dp[amount]


c = [int(x) for x in input().split()]
a = int(input())
print(coinChange(c, a))
