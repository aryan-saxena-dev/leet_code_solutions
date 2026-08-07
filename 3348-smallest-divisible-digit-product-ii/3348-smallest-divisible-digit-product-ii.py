from math import gcd

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        rest = t
        for p in (2, 3, 5, 7):
            while rest % p == 0:
                rest //= p
        if rest != 1:
            return "-1"

        def tail(r):
            """Fewest / lexicographically smallest digits whose product covers r."""
            out = []
            while r > 1:
                bd, bg = 1, 1
                for d in range(2, 10):          # ascending -> smallest digit wins ties
                    g = gcd(r, d)
                    if g > bg:
                        bg, bd = g, d
                out.append(bd)
                r //= bg
            return out[::-1]                    # first picked sits rightmost

        n = len(num)
        z = num.find('0')
        limit = n - 1 if z == -1 else z

        # prefix remainders: pre[i] = t left after consuming num[:i]
        pre = [t] * (n + 1)
        r = t
        for i, ch in enumerate(num):
            if ch == '0':
                break
            r //= gcd(r, int(ch))
            pre[i + 1] = r

        if z == -1 and pre[n] == 1:
            return num

        for i in range(limit, -1, -1):
            r0 = pre[i]
            for d in range(int(num[i]) + 1, 10):
                suf = tail(r0 // gcd(r0, d))
                if len(suf) <= n - 1 - i:
                    s = ''.join(map(str, suf))
                    return num[:i] + str(d) + '1' * (n - 1 - i - len(s)) + s

        suf = tail(t)
        L = max(n + 1, len(suf))
        s = ''.join(map(str, suf))
        return '1' * (L - len(s)) + s