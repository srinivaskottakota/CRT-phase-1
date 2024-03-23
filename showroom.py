class showroom:
    def __init__(self):
        self.sgst=5555
        self.cgst=5555
        self.insurance=100000
    def company(self):
        while True:
            self.n=input("Enter Company name:")
            if self.n == "Toyato":
                print("Welcome to ",self.n)
                self.n=self.model()
                break
            elif self.n == "Mercedes":
                print("Welcome to company ",self.n)
                self.n=self.model()
                break
            elif self.n == "Mahindra":
                print("Welcome to compamu ",self.n)
                self.n=self.model()
            else:
                print("Re-Enter valid company name!!")
    def model(self):
        while True:
            self.m=input("Enter Model name: ")
            if self.m == "Fortuner":
                self.car_price(self.m)
                break   
            elif self.m == "Ertiga":
                self.car_price(self.m)
                break
            elif self.m == "Scorpio":
                self.car_price(self.m)
                break
            elif self.m == "Thar":
                self.car_price(self.m)
                break
            elif self.m == "Lc":
                self.car_price(self.m)
                break
            elif self.m == "Suv":
                self.car_price(self.m)
                break
            else:
                print("Re enter vaild Model Name")
    def car_price(self,m):
        if m == "Fortuner":
            self.price=4500000
        elif m == "Ertiga":
            self.price=3000000
        elif m == "Scorpio":
            self.price=4000000
        elif m == "Thar":
            self.price=3500000
        elif m == "Lc":
            self.price=3200000
        elif m == "Suv":
            self.price=4500067
        tot_price = self.price + self.sgst +self.cgst + self.insurance
        print("On ROad Price of the model is ",tot_price)
    
obj = showroom()
obj.company()