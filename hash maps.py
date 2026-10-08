class solution:
    def Two_sum(self,nums,target):
        seen={}
        for i,n in enumerate(nums):
            needed=target-n
            if needed in seen:
                return seen[needed],i
            seen[n]=i

nums=[2,4,6,1,5,8,9]
target=5
obj=solution()
print(obj.Two_sum(nums,target))