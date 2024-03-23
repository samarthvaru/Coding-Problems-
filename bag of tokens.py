class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i,j = 0, len(tokens)-1
        points = maxPoints = 0
        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                points+=1
                maxPoints = max(maxPoints,points)
                i+=1
            elif points>0:
                points-=1
                power+=tokens[j]
                j-=1
            else:
                return maxPoints
        
        return maxPoints
        
