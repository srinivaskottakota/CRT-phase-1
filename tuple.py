mytuple=("Jahnavi","Siri",1,5,3,"u9",12.456)
print(mytuple)
print(type(mytuple))
mytuple = mytuple + ("kishore",)
print(mytuple)
mytuple=mytuple+("hello",56)
print(mytuple)


for i in range (0,5):
    n=int(input("Enter a numbele"))
    mytuple = mytuple + (n,)
print(mytuple)