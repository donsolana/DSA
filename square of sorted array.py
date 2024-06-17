class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        i = len(nums) - 1
        n = len(nums)
        l = 0
        r =  len(nums) - 1
        for i in range(n-1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r]
                r -=1
            else:
                square = nums[l]
                l += 1
           
            print(i)
            print(square)
            result[i] = square * square
            i -= 1
        return result
