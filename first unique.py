def unique_numbers(nums):
    seen={}
    for n in nums:
        seen[n]=seen.get(n,0)+1

    for key,values in seen.items():
        if values==1:
            return key #OR
        #if seen[values]==1:
         #   return seen[key]
        #print(f"the unique number is {seen[n]}")
nums=[2,5,7,3,4,2,7,2,5,7,4]
print(unique_numbers(nums))