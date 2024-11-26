'''A pronic number is a figurate number
that is the product of two consecutive
integers. The first few pronic numbers are:
2, 6, 12, 20, 30, 42, 56, 72, 90, and 110. 
 
Pronic numbers are also known as
oblong, heteromecic, or rectangular
numbers. The study of pronic numbers
dates back to Aristotle.
'''
n=72
status=False
for i in range(1,n):
    if (i*(i+1))==n:
        status=True
        break
if status:
    print("Yes pronic No ")
    print(i,i+1,"=",n)
else:
    print("No pronic No ")
print(n)    