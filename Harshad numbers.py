'''Check Harshad Number
Here are some examples of Harshad numbers: 
18: The sum of the digits of 18 is 9, and 18 is divisible by 9. 
1729: The sum of the digits of 1729 is 19, and 1729 is divisible by 19. 
200: The sum of the digits of 200 is 0, and 200 is divisible by 0. 
54: The sum of the digits of 54 is 9, and 54 is divisible by 9. 
A Harshad number is a positive integer that is divisible
by the sum of its digits.
They are also called Niven numbers or multidigital numbers. 

'''
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10
if num % sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")