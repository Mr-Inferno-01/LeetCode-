class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
       
        look = {}


        for i in range(len(nums)):
            required_nums = target - nums[i]

            if  required_nums in look:
                return[look[required_nums] , i]

            look[nums[i]] = i

                

        
       
