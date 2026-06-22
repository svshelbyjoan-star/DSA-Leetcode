class Solution(object):
    def removeDuplicates(self, nums):
        l = 0
        r = 1
        while r<len(nums):
            if nums[l] == nums[r]:
                nums.remove(nums[r])
            else:
                r+=1
                l+=1
        print(len(nums))
        print(nums)
        