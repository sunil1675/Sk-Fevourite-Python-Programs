#s=input("Enter a String ")
s="The quick brown fox jumps over the lazy dog"
import string

status=True
for i in s:
    if i not  in string.ascii_letters+" ":
        status=False
        print(i)
        
if status:
    print(status,'yes pangram')
else:
    print(status,'Not pangram')
    
        