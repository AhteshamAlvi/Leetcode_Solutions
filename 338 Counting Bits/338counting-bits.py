class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        x = 0
        while 2**x < n + 1:
            block = 2**x
            start = block
            end = min(2**(x + 1), n + 1)

            for j in range(start, end):
                ans[j] = ans[j - block] + 1

            x+=1

        return ans