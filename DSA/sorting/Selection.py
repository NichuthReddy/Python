class Solution:
    def selectionSort(self, nums):
        len_nums=len(nums)
        for i in range(0,len_nums+1):
            for j in range(1,len_nums+1):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums

    selectsort = Solution

    nums = [5, 2, 9, 1, 5, 6]
    
    selectsort.selectionsort(nums)