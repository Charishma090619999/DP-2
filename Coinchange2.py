#Time complexity: O(n*amount)
#Space complexity: O(n*amount)
class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0]=1
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j-coins[i-1]<0:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
        return dp[-1][-1]