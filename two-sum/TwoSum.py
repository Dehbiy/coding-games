from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            diffrence = target - nums[i]
            if diffrence in nums_dict:
                return [nums_dict[diffrence], i]
            nums_dict[nums[i]] = i

    def bruteForcetwoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
if __name__ == '__main__':
    nums=[3,4,5,6]
    target=7
    output = TwoSum().twoSum(nums, target)
    print(f"your output = {output}\nexpected output [0, 1]")
        