class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sums=0
        for i in nums:
            sums+=i
        tot=n*(n+1)/2
        return int(tot-sums)