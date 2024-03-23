n=153
nod = 0
n1 = n
org = n
sum=0
while n>0:
    n=n//10
    nod=nod+1
while n1>0:
    d=n1%10
    sum=sum+d**nod
    n1 = n1//10
if sum==org:
    print("Yes")
else:
    print("No")


