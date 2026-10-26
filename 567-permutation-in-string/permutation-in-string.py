class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = {}
        freq_s2 = {}

        for char in s1:
            freq_s1[char] = freq_s1.get(char, 0) + 1

        for k in range(len(s1)):
            ch = s2[k]
            freq_s2[ch] = freq_s2.get(ch, 0) + 1
        if freq_s1 == freq_s2:
            return True

        for right in range(len(s1), len(s2)):
            ch = s2[right]
            freq_s2[ch] = freq_s2.get(ch, 0) + 1
            out = s2[right - len(s1)]
            freq_s2[out] -= 1
            if freq_s2[out] == 0:
                del freq_s2[out]
            if freq_s1 == freq_s2:
                return True
        return False

        
            

            


