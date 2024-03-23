def p(n,m):
    if m==0:
        return 1
    return n*p(n,m-1)
a=p(2,3)
print("Power:",a)