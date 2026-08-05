from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)

        # 1. mark everything reachable from k
        suspicious = [False] * n
        suspicious[k] = True
        stack = [k]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if not suspicious[u]:
                    suspicious[u] = True
                    stack.append(u)

        # 2. an outside method calling into the group blocks removal
        for a, b in invocations:
            if suspicious[b] and not suspicious[a]:
                return list(range(n))

        # 3. keep the rest
        return [i for i in range(n) if not suspicious[i]]