class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = nums

        n = len(nums)
        arr += [None] * n
        for i in range(n):
            arr[n + i] = nums[i]

        return arr


        