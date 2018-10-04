class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            second_number = target - nums[i]
            try:
                j= nums.index(second_number,i+1)
                break
            except ValueError as e:
                continue
        return [i,j]

obj = Solution()
nums = [-3,4,3,90]
result = obj.twoSum(nums, 0)
print(result)