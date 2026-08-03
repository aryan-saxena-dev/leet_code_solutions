class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] = best score difference for the player to move at index i
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take = 0
            best = float('-inf')
            for k in range(3):
                if i + k >= n:
                    break
                take += stoneValue[i + k]
                best = max(best, take - dp[i + k + 1])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"