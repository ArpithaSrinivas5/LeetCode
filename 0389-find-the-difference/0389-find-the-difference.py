class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s = Counter(s)
        
        for letter in t:
            if letter not in freq_s:
                return letter
            freq_s[letter] -=1
            
            if freq_s[letter] ==0:
                del freq_s[letter]
                