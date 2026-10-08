def subarray(lists):
    current_sum=0
    max_sum=0
    for l in lists:
        current_sum=max(current_sum+l,l)
        max_sum=max(max_sum,current_sum)
    return max_sum
lists=[1,-3,-2,8]
print(subarray(lists))
