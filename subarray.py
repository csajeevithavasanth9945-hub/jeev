a=[1,-3,-2,8]
current_sum=0
best_sum=0
for nums in a:
    current_sum = max(nums,current_sum+nums)
    best_sum=max(best_sum,current_sum)
print(best_sum)

# 1 