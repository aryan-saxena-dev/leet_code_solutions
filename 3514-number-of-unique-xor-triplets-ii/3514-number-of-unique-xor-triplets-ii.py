class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = list(set(nums))
        SIZE = 2048  # values < 2^11, so all XORs fit here

        pair = bytearray(SIZE)
        for x in vals:
            for y in vals:
                pair[x ^ y] = 1

        pair_vals = [i for i in range(SIZE) if pair[i]]

        res = bytearray(SIZE)
        for p in pair_vals:
            for y in vals:
                res[p ^ y] = 1

        return sum(res)