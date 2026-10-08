def duplicates(n):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]==n[j]:
                return [i,j]
n=[1,2,3,4,5,6,7,3,7,9,2]
print(duplicates(n))