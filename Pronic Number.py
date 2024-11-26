'''Check Pronic Number
The first few Pronic numbers are: 
0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462 
Pronic number is a number which is the product
of two consecutive integers, that is,
a number n is a product of x and (x+1). 
'''

num = int(input("Enter a number: "))
flag = False
for i in range(1, num):
    If the product of `i` and `(i + 1)` equals `num`, then...
        flag = True
        break
if flag:
    print("Pronic Number")
else:
    print("Not Pronic Number")