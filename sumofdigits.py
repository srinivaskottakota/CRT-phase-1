n=21
sd=0
a=n
while n>0:
    d=n%10
    sd=sd+d
    n=n//10
if a%sd==0:
    print("Divisible")
else:
    print("Not divisible")
