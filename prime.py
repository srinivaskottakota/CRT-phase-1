def isprime():
    n=int(input("Enter a number:"))
    f=1
    for i in range(2,n):
        if n%i==0:
            f=0
            break
    if f==1:
        print("Prime")
    else:
        print("Not Prime")

isprime()