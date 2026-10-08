a=int(input("Enter the digits:"))
#123 1+2+3=5
#original=a
reverse=0
while a !=0:
    digit=a%10
    a=a//10
    reverse=(reverse*10)+digit
#if original == reverse:
 #   print(f"yes this {reverse} is a palindrome")
#else:
 #   print("this number is not a palindrome")
print(reverse)
