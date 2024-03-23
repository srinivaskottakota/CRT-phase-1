# class f15:
#     def light(self):
#         print("Lights on")
#     def fan(self,speed):
#         print("Fans on speed is ",speed)
#         self.s=speed
#     def cpu(self):
#         print("System on")
#         print("are u comfortable with this speed ",self.s)
# #objectname = classname()
# obj = f15()
# #objectname.functionname()
# obj.light()
# obj.fan(5)
# obj.cpu()


# class f16(f15):
#     def __init__(self,a):
#         self.a=a
#         print("Welcome to Strides")
#     def prgm(self,speech):
#         self.speech=speech
#         print("Time to give speech on ",speech)
#     def display1(self):
#         print("The program is succesffuly completed")


# class shopping(f15):
#     def __init__(self,place):
#         self.place = place
#         print("Welecome to ",place)
#     def dtype(self,dt):
#         self.dt=dt
#     def price(self,prices):
#         self.p=prices


#     def size(self,sizes):
#         self.s=sizes
#     def display(self):
#         print(self.dt,self.p,self.s)
# user = shopping(123,123)
# user.dtype("Shirt")
# user.price(3000)
# user.size("L")
# user.display()
# user.fan(5)
# user.light()
# user.cpu()
# user.display1()