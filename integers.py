a=123
reversed=0
while a!=0:
    integer=a%10
    reversed=reversed*10+integer
    a=a//10
print(reversed)
