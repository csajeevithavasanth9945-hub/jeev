lists=int(input("Enter the digits:"))
original=lists
reversed=0
while lists!=0:
    digits=lists%10
    reversed=reversed*10+digits
    lists=lists//10

if original==reversed:
    print("palindrome")
else:
    print("not palindrome")
