from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = sorted(Counter(word).values(), reverse=True)
        total = 0
        for i, f in enumerate(freqs):
            total += f * (i // 8 + 1)
        return total