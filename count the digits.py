class Solution:
    def count_frequency(self,nums):
        seen={}
        for n in nums:
            seen[n]=seen.get(n,0)+1
        return seen
        # print(seen)
nums=[2,6,2,9,5,4,6,1,7,5,2,5]
obj=Solution()#The () after Solution means create an instance/object of that class.
print(obj.count_frequency(nums))#obj is the object that gives you access to the methods (functions) inside Solution.