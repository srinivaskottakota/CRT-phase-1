L1=[1,34,"Hi!!",True,90]
print(L1)
L1.append("Siri")
print(L1)
L1.insert(3,6)
print(L1)
print(L1[2])
print(L1[4])
print(type(L1))
for i in range (0,len(L1)):
    print(L1[i])

for i in L1:
    print(i)

print(L1[:3])
print(L1[0::2])
print(L1[6:0:-1])
print(L1[::])
print(L1[2::3])
print(len(L1))

L1[3]="Srinivas"
print(L1)
