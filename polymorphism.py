#Function over riding
# class Father:
#     def bike(self):
#         print("Harley Dividson")
#     def laptop(self):
#         print("Laptop with 2gb ram")
# class krishna(Father):
#     def laptop(self):
#         print("I want new version laptop")
#         print("16Gb ram with tuffgaming and high requirements")
# obj=krishna()
# obj.laptop()
# obj.bike()

#Constructor overriding
class Father():
    def __init__(self):
        print("Go to Hostel")
class Child(Father):
    def __init__(self):
        print("No I will go tommorow dad")
        print("Thank you")
obj=Child()
obj.Child()
obj.Father()