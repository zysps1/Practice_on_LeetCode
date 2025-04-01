class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         temp_target = nums[i] + nums[j]
        #         if temp_target == target and i != j:
        #             return [i, j]

        save_set = []
        for i in range(len(nums)):
            if target - nums[i] in save_set:
                return [nums.index(target - nums[i]), i]
            save_set.append(nums[i])