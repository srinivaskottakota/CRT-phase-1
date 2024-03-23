def check(n):
    if n%10==5:
        return n*check(1)
    # elif n%10==3:
    #     return n*check()
a=check(15)
print(a)