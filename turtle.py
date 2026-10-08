#Here are problems that reuse the same `%` / `//` digit-extraction pattern you just learned — good practice to make it stick.

#**1. Reverse a Number**
#Given `1234`, print it reversed as `4321` — without converting to a string. (Hint: same loop, but instead of *adding* digits to a total, think about how you'd *build* a new number digit by digit. What operation would place a digit into the next position — think about multiplying by 10.)

#**2. Count the Digits**
#Given a number like `54321`, count how many digits it has (answer: 5) — without using `len(str(number))`. Same loop shape as sum-of-digits, but what are you counting instead of summing?

#**3. Palindrome Number Checker**
#Given a number like `12321`, check if it reads the same forwards and backwards. (Hint: this combines Problem 1 — reverse the number — with a simple comparison at the end.)

#**4. Armstrong Number Checker**
#An Armstrong number is one where the sum of its digits, each raised to the power of the total digit count, equals the number itself. Example: `153 = 1³ + 5³ + 3³`. (Hint: you'll need Problem 2's digit count, combined with the sum-of-digits loop — but raising each digit to a power instead of just adding it.)

#**5. Extract Only Even Digits**
#Given a number like `123456`, find the sum of only its *even* digits (2+4+6 = 12). Same loop, but add a condition inside checking if the digit is even before adding it.

#**6. Find the Largest Digit**
#Given a number like `4829`, find its largest single digit (answer: 9) — without converting to a string or list. (Hint: similar tracking-a-value pattern as before, but instead of adding to `total`, you're comparing and keeping the bigger one.)

#**7. Digit Root**
#Keep summing the digits of a number repeatedly until you're left with a single digit. Example: `9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2`. (Hint: you already know how to sum digits once — now think about when you'd need to repeat that *entire* process again.)

#Try **#1 (Reverse a Number)** first since it's closest to what we just did — tell me your plain-English steps before writing code, same as before.