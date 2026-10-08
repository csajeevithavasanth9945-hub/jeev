lists=[9,22,20,30,100,19]
for i in range(len(lists)):
    is_max=True
    for j in range(len(lists)):
        if j!=i and lists[i] < lists[j]:
            is_max=False
            break
    if is_max:
        print(lists[i])  
                
    

# 9[0] 22[1] 20[2] 19[3] -->i
# 22[1] 20[2] 19[3] --j
#9<22 yes 22<20 no 20<19 no 