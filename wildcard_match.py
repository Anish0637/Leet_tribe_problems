class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        m,n = len(s),len(p)
        cnt =p.count('*')
        if n - cnt > m:
            return False
        
        dp=[True] + [False]*n

        for j in range(1,n+1):
            dp[j]= dp[j-1] and p[j-1]=='*'
        
        for i in range(1,m+1):
            cur=[False]*(n+1)
            for j in range(1,n+1):
                if p[j-1]=='*':
                    cur[j]= cur[j-1] or dp[j]
                elif p[j-1]==s[i-1] or p[j-1]=='?':                   
                    cur[j]=dp[j-1]   
            dp=cur
        return dp[n]

cl=Solution()
cl.isMatch("ab", "?*")   
cl.isMatch("aa", "a")
cl.isMatch("aa", "*") 
cl.isMatch("aa", "a*") 
cl.isMatch("ab", "?*") 
cl.isMatch("aab", "c*a*b")  


