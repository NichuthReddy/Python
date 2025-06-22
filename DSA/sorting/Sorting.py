class Solution:
    def selectionSort(self, nums):
        len_nums=len(nums)
        for i in range(0,len_nums-1):
            for j in range(i+1,len_nums):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        print(f"selection sort ouput: {nums}")

    def bubbleSort(self, nums):
        n = len(nums)
        for f in range(n-1,0,-1):
            for i in range(0, f):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        
        print(f"bubble sort ouput: {nums}")

    def insertionSort(self, nums):
        n=len(nums)
        for i in range(1,n):
            for j in range(i,0,-1):
                if nums[j-1]>nums[j]:
                    nums[j-1],nums[j] = nums[j],nums[j-1]
        
        print(f"insertion sort ouput: {nums}")

    def mergeSort(self, nums, low, high):
        def Merge(nums, low, mid, high):
            l=low
            r=mid+1
            temp= []
            while l<=mid and r<=high:
                if nums[l]<=nums[r]:
                    temp.append(nums[l])
                    l+=1
                else:
                    temp.append(nums[r])
                    r+=1
            while l<=mid:
                temp.append(nums[l])
                l+=1

            while r<=high:
                temp.append(nums[r])
                r+=1
            for i in range(low,high+1):
                nums[i] = temp[i-low]

        #Logic starts from here        
        if low>=high: return
        mid = (low+high)//2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid+1, high)
        Merge(nums,low, mid, high)
        #only print when top level Merge call is returned
        if low==0 and high==len(nums)-1:
            print(f"merge sort output: {nums}")

    def quickSort(self,nums, low, high):
        if low >= high: return
        pindex = low
        l = low
        r = high
        while l<=r:
            while nums[pindex]>=nums[l] and l<=r:
                l+=1
            while nums[pindex]<nums[r] and l<=r:
                r-=1
            if l>r:
                break
            nums[l],nums[r] = nums[r],nums[l]
        nums[pindex],nums[r] = nums[r],nums[pindex]
        self.quickSort(nums, low, r-1)
        self.quickSort(nums, r+1, high)
        if low == 0 and high == len(nums)-1:
            print(f"quick sort output: {nums}")


sort = Solution()

qnums = [5, 2, 9, 1, 5, 6, 3, 10] #testing
sort.quickSort(qnums,0,7)

snums = [5, 2, 9, 1, 5, 6, 3, 10] #testing
sort.selectionSort(snums)

bnums = [5, 2, 9, 1, 5, 6, 3, 10]
sort.bubbleSort(bnums)

inums = [5, 2, 9, 1, 5, 6, 3, 10]
sort.insertionSort(inums)

mnums = [5, 2, 9, 1, 5, 6, 3, 10]
sort.mergeSort(mnums,0,7)
