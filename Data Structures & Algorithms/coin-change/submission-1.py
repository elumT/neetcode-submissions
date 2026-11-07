class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = (amount + 1) * [amount + 1]
        d[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if c <= a:
                    d[a] = min(d[a], d[a-c] + 1)
        return d[amount] if d[amount] != amount + 1 else -1
        