a=[0,2,6,9,0,3]
new_list=[]
for nums in a :
    if nums>0:
        new_list.append(nums)
count=a.count(0)
new_list.extend([0]*count)
print(new_list)
