list=[42,36,28,96,4,-1,1]
min=999
max=-999
#print("Sum",min(list)+max(list))
for i in range(0,len(list)):
    if list[i]<min:
        min=list[i]
    elif list[i]>max:
        max=list[i]
print(min+max)
