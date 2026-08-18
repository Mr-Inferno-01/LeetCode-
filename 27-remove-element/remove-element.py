class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k  =  0

        for ind in range(len(nums)):
            if nums[ind] != val:
                nums[k] = nums[ind]

                k += 1
        return k