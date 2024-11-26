'''A strong number is a number that is equal to
the sum of the factorials of its digits: 
Explanation: For example, 145 is a
strong number because 1! + 4! + 5! = 1 + 24 + 120 = 145. 
Examples: Some other examples
of strong numbers include 1, 2, and 40,585. '''

n=input("Enter a NUmber ")

tot=0
for i in n:
    t=int(i)
    f=1
    for j in range(1,t+1):  # factorial code
        f=f*j
    tot=tot+f

if tot==int(n):
    print(tot,"yes it is strong no")
else:
    print(tot,"NO it is not strong no")
        
    
    
    









