class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = {}

        # Count frequency
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        left = []
        middle = ""

        # Characters in sorted order
        for ch in sorted(freq.keys()):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2 == 1:
                middle = ch

        left = "".join(left)

        return left + middle + left[::-1]