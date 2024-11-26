'''An example of a disarium number is 135.
A disarium number is a number where the sum
of the digits to the power of their
respective position is equal to the number
itself. For 135, this is true
because: 135 = 11 + 32 + 53 and 135 = 1^(1) + 3^(2) + 5^(3)
'''
num = int(input("Enter a number: "))
sum = 0
length = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    length -= 1
    temp //= 10

if sum == num:
    print("Disarium Number")
else:
    print("Not Disarium Number")
