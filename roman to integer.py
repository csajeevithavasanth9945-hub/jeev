roman_number=input("Enter the roman number:")
roman_values={
    'I':1,
    'V':2,
    'X':5,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
total=0
for i in range(roman_number):
    if i+1<roman_number:
        print