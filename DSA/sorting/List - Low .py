#low
class Solution:
    def largestElement(self, nums):
        len_nums =len(nums)
        largest = nums[0] #S -> O(1)
        for i in range(1,len_nums-1): #T -> O(n)
            if nums[i-1]<nums[i]:
                largest=nums[i]
        print(f"largest element in the {nums} is {largest}")

    def secondLargestElement(self, nums):
        len_nums =len(nums)
        largest=nums[0]
        second_largest= float('-inf')
        for i in range(1,len_nums):
            if second_largest<nums[i] and nums[i]!= largest:
                second_largest= nums[i]
            if nums[i]>largest:
                largest= nums[i]
                second_largest= largest
        print(f"second largest element in the {nums} is {second_largest}")

    def nthLargestElement(self, nums):
        #quicksort
        def quicksort(nums, low, high):
            if low>=high: return
            pindex = low
            l=low+1
            r=high
            while l<=r:
                while l<=r and nums[l]<= nums[pindex]:
                    l+=1
                while l<=r and nums[r] > nums[pindex]:
                    r-=1
                if l>r:
                    break
                nums[l],nums[r] = nums[r],nums[l]
            nums[pindex],nums[r] = nums[r],nums[pindex]

            quicksort(nums, low, r-1)
            quicksort(nums, r+1, high)
        
        len_nums=len(nums)
        low=0
        high =len_nums-1
        quicksort(nums, low, high)
        nthlargestindex=1
        nthlargestnum=nums[-1]
        for i in range(len_nums-1,0,-1):    
            if nthlargestnum!=nums[i]:
                nthlargestnum=nums[i]
                nthlargestindex+=1
            if nthlargestindex==2:
                print(f"{nthlargestindex}th largest number in {nums} is {nthlargestnum}")

    def isSortedList(self, nums):
        len_nums=len(nums)
        asc=1
        desc=1
        for i in range(1,len_nums):
            if nums[i-1]<=nums[i]:
                pass
            else:
                asc=0
            
            if nums[i-1]>=nums[i]:
                pass
            else:
                desc=0
        if asc==1:
           order="in ascending order"
        elif desc==1:
            order="in descending order"
        else:
            order="not sorted" 
        print(f"{nums} is {order}")

    # input ascending: [0,0,2,2,2,3,4,4,4] ouput: [0,2,3,4,2,3,4,4,4], 4(unique elements)
    def removeDuplicates(self, nums):
        len_nums=len(nums)
        f=0
        for m in range(1, len_nums):
            if nums[f]<nums[m]:
                nums[f+1]=nums[m]
                f+=1
        print("remove Duplicates:",nums,f+1)

    # input: [1,2,3,4] output:[2,3,4,1]
    def rotateListByOne(self, nums):
        len_nums=len(nums)
        temp = nums[0]
        org_nums=nums[:]
        for i in range(1,len_nums):
            nums[i-1]=nums[i]
        nums[-1]=temp
        print(f"left rotate {org_nums} by 1 element is {nums}")

    def rotateListByDelements(self, nums, d):
        len_nums=len(nums)
        d= d % len_nums
        org_nums=nums[:]
        #temp = nums[0:d]
        temp=[]
        for i in range(0,d):
            temp.append(nums[i])

        for j in range(d,len_nums):
            nums[j-d]=nums[j]
        
        for k in range(0,d):
            nums[len_nums-d+k]=temp[k]

        print(f"left rotate {org_nums} by {d} element is {nums}")

    # input: [1,4,0,0,5,0,6] output: [1,4,5,6,0,0,0]
    def moveZeroes(self, nums):
        org_nums=nums[:]
        len_nums=len(nums)
        j=-1
        for i in range(0,len_nums):
            if nums[i]==0 and j==-1:
                j=i
            elif nums[i]!=0 and j!=-1:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        print(f"movezeroes of {org_nums} is {nums}")

    # input find 1st occurence index of the target in the list if not found return -1
    def linearSearch(self, nums, target):
        len_nums=len(nums)
        for i in range(0,len_nums):
            if nums[i]==target:
                return i
        return -1

    def unionList(self, nums1, nums2):
        len_nums1=len(nums1)
        len_nums2=len(nums2)
        i=j=0
        union_result=[]
        while True:
            if i>len_nums1-1 or j>len_nums2-1:
                break
            if nums1[i]<=nums2[j]:
                if not union_result or  union_result[-1]!=nums1[i]:
                    union_result.append(nums1[i])
                i+=1
            else:
                if not union_result or union_result[-1]!=nums2[j]:
                    union_result.append(nums2[j])
                j+=1

        while i<=len_nums1-1:
            if union_result[-1]!=nums1[i]:
                union_result.append(nums1[i])
            i+=1
        while j<=len_nums2-1:
            if union_result[-1]!=nums2[j]:
                union_result.append(nums2[j])
            j+=1

        print(f"union of {nums1} and {nums2} is {union_result}")

    # missing number in a 0 to n list if not is missing return n+1
    def missingNumber(self, nums): # TC -> O(n+logn base2), SC -> O(1)
        def quicksort(nums, low, high):
            if low>=high: return
            pivot=low
            l=low+1
            r=high
            while True:
                if l<=r and nums[l]<=nums[pivot]:
                    l+=1
                if l<=r and nums[r]>nums[pivot]:
                    r-=1
                if l>r:
                    break
                nums[l],nums[r]=nums[r],nums[l]
            nums[pivot],nums[r]=nums[r],nums[pivot]
            quicksort(nums,low,r-1)
            quicksort(nums,r+1,high)
        low=0
        len_nums=len(nums)
        high=len_nums-1
        org_nums=nums[:]
        quicksort(nums,low,high) #TC -> )(logn base2), SC-> )(1)
        if nums[0]!=0:
            print(f"missing number in {org_nums} is 0")
            return 0
        for i in range(1,len_nums): #TC -> O(n), SC -> O(1)
            if nums[i]-nums[i-1]!=1:
                print(f"missing number in {org_nums} is {nums[i]-1}")
                return nums[i]-1
        print(f"missing number in {org_nums} is {nums[-1]+1}")
        return nums[-1]+1
    
    def missingNumberOptimal(self, nums):
        len_nums = len(nums)
        max=0
        sum_nums=0
        isZero=0
        for i in range(0,len_nums):
            if nums[i]>max:
                max=nums[i]
            sum_nums+=nums[i]
            if nums[i]==0:
                isZero=1

        sum_1tomax = max*(max+1)/2
        result = int(sum_1tomax-sum_nums)
        if isZero==0:
            print(f"missing number in {nums} is 0")
        elif result==0:
            print(f"missing number in {nums} is {max+1}")
        else:
            print(f"missing number in {nums} is {result}")

    # nums = [1,1,0,0,1,1,1,0,0,1,1], output: 3
    def maxConsecutiveOnes(self, nums):
        len_nums = len(nums)
        maxi=0
        current_max=0
        for num in nums: #Time Complexity(TC) -> O(n), Space Complexity -> O(1)
            if num==1:
                current_max+=num
            else:
                maxi=max(maxi,current_max)
                current_max=0
        maxi=max(maxi,current_max)
        print(f"maximum consecutive ones in {nums} is {maxi}")

    # Appear once in a list [3,4,1,3,4,5,5](other elements appear twice) output: 1
    def appearOnce(self, nums): # TC ->O(n+n/2) SC ->O(n/2+1)
        counter = {}
        for num in nums:   # TC -> O(n) SC ->O(n/2+1)
            counter[num]=counter.get(num,0)+1
        for key,value in counter.items(): # TC -> O(n/2+1) SC ->O(1)
            if value==1:
                print(f"Element which appears once in {nums} is {key}")
                return
        print(f"No element appears once in {nums}")

    def appearOnceOptimal(self, nums):
        xor=0
        for num in nums: # TC -> O(n), SC -> O(1)
            xor^=num
        print(f"Element which appears once in {nums} is {xor}")

    #longest subarray length in nums(positive number) with sum as k
    def longestPositiveSubList(self, nums, k):
        len_nums = len(nums)
        i=0
        sum=0
        max_length=0
        no_of_sublists=0
        sublists=[]
        for j in range(0,len_nums):
            sum+=nums[j]
            while sum>k and i<=j:
                sum-=nums[i]
                i+=1
            if sum==k:
                sublists.append(nums[i:j+1])
                no_of_sublists+=1
                max_length=max(max_length,j-i+1)
        print(f"longest positive subarray length in {nums} with sum as {k} is\nmax_length: {max_length}\tsublists: {sublists}\tno_of_sublists: {no_of_sublists}")


    def longestSubList(self, nums, k):
        len_nums=len(nums)
        sum=0
        sum_dict_positions={}
        max_length=0
        no_of_sublists=0
        sublists=[]
        for p in range(0,len_nums):
            sum+=nums[p]
            if sum==k:
                max_length=max(max_length,p)
                sublists.append(nums[0:p+1])
                no_of_sublists+=1

            if sum not in sum_dict_positions:
                sum_dict_positions[sum]=p

            rem=sum-k
            if rem in sum_dict_positions:
                max_length=max(max_length, p-sum_dict_positions[rem])
                sublists.append(nums[sum_dict_positions[rem]+1:p+1])
                no_of_sublists+=1

        print(f"longest subarray length in {nums} with sum as {k} is\nmax_length: {max_length}\tsublists: {sublists}\tno_of_sublists: {no_of_sublists}")



        


            


sol =Solution() 

lnums =[2,8,4,3,5]
sol.largestElement(lnums)

snums =[8,8,4,3,5]
sol.secondLargestElement(snums)
nnums=[8,8,4,3,5]
sol.nthLargestElement(nnums)

isnums=[8,2,1,0]
sol.isSortedList(isnums)

rdnums=[0,0,2,2,2,3,4,4,4]
sol.removeDuplicates(rdnums)

lrnums=[1,2,3,4,5]
sol.rotateListByOne(lrnums)

lrdnums=[1,2,3,4,5,6]
sol.rotateListByDelements(lrdnums,14)

mznums=[1,4,0,0,5,0,6,0]
sol.moveZeroes(mznums)

lsnums=[1,2,3,4,2,3,4]
target=3
print(f"first occurance of {target} in {lsnums} is {sol.linearSearch(lsnums,target)}")

unum1=[1,2,2,3,4,5]
unum2=[2,3,6,7]
sol.unionList(unum1,unum2)

mnnums=[4,2,3,1,0,5]
sol.missingNumber(mnnums)

mnonums=[4,2,3,0,5]
sol.missingNumberOptimal(mnonums)

mconums=[1,1,0,1,1,1,0,0,1,1]
sol.maxConsecutiveOnes(mconums)

aonums=[3,4,1,1,3,4,5,5]
sol.appearOnce(aonums)

aoonums=[3,4,1,3,4,5,5]
sol.appearOnceOptimal(aoonums)

lpsnums=[1,2,3,4,0,1,2,1,0,3,0,0,1,1,1]
k=3
sol.longestPositiveSubList(lpsnums, k) # will miss some -ve scenarios

lsnums=[1,2,3,4,0,1,2,1,-1,0,3,0,0,1,1,1]
k=3
sol.longestSubList(lsnums, k)
