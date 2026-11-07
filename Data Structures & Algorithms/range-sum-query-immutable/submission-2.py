class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            return 0
        n = len(self.nums)
        if left > n or right > n:
            return 0 
        count = 0
        for i in range(left, right+1):
            count += self.nums[i]
        return count
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)