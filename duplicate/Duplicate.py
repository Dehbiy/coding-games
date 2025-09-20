from typing import List


'''
Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true


Example 2:

Input: nums = [1, 2, 3, 4]

Output: false


'''

class Duplicate:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return False
            seen.add(num)
        return True

    def oneLinehasDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
        
if __name__ == '__main__':
    nums=[3,4,5,6]
    output = Duplicate().hasDuplicate(nums)
    print(f"your output = {output}\nexpected output True")
        