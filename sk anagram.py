# function to check if two strings are  anagram or not 
s1=input("Enter a String ")             # "listen"
s2=input("Enter a String ")             #"silent" 

if(sorted(s1)== sorted(s2)):
     print("The strings are anagrams.") 
else:
     print("The strings aren't anagrams.")         
        

