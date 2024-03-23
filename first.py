'''''def u(s):
    return s.upper()
def sm(s):
    return s.lower()
def abc(func,s):
    return func(s)
print(abc(u,"hsdfvb"))
print(abc(sm,"dbBHDFBF"))
'''''

'''def fun(s1):
    def count(s2):
        return s1+s2
    return count
x=fun('abc')
print(x('pqr'))'''

'''def decorator(func):
    def inner():
        print('abc')
        func()
        print("after x func call")
    return inner
def x():
    print("x function")
i=decorator(x)
i()'''


'''
s1=input('enter first name:').strip()
s2=input('enter second name:').strip()
dup=set(s1).intersection(set(s2))
print(dup)
count=0
for i in s1+s2:
    if i not in dup:
        count+=1
print(count)'''

s1=input('enter first name:').strip()
s2=input('enter second name:').strip()
s1=list(s1)
s2=list(s2)
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            s1[i]='0'
            s2[j]='0'
            break
count=0
for i in s1+s2:
    if i!=0:
        count+=1
print(count)