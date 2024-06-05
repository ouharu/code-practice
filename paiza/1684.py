from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0
        
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                count += 1
            
        return count
    
allowed = "ab"

words = ["ad","bd","aaab","baa","badab"]

solution = Solution()

print(solution.countConsistentStrings(allowed,words))