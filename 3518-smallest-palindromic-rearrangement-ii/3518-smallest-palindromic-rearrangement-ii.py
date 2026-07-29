from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 5

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [f // 2 for f in freq]
        half_len = sum(half)

        mid = ""
        for i in range(26):
            if freq[i] % 2:
                mid = chr(ord('a') + i)
                break

        def count_ways(cnt):
            rem = sum(cnt)
            ways = 1
            for x in cnt:
                if x:
                    ways *= comb(rem, x)
                    if ways >= LIMIT:
                        return LIMIT
                    rem -= x
            return ways

        if count_ways(half) < k:
            return ""

        first = []

        for _ in range(half_len):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = count_ways(half)

                if ways >= k:
                    first.append(chr(ord('a') + c))
                    break

                k -= ways
                half[c] += 1

        first = "".join(first)
        return first + mid + first[::-1]