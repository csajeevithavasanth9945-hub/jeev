string=input("enter the string")
vowels="aeiou"
count=0
for i in range(len(vowels)):
    for j in range(len(string)):
        if vowels[i] in string[j]:
            count+=1
print(count)