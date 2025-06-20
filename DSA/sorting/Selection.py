class Solution:
    def selectionSort(self, nums):
        len_nums=len(nums)
        for i in range(0,len_nums-1):
            for j in range(i+1,len_nums):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums

selectsort = Solution()

nums = [5, 2, 9, 1, 5, 6, 3, 10] #testing
print("Testing Selection Sort")
print(selectsort.selectionSort(nums))