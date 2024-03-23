n=int(input("Enter a Number:"))
a=n
rev=0
while n>0:
    d=n%10
    n=n//10
    rev=rev*10+d
if a==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
    
