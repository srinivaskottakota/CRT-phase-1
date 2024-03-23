class showroom:
    def company(self,company):
        l=["Toyota","Mahindra"]
        if company in l:
            print("Welcom to ",company)
    def model(self,company):
        d=["Toyota":["Fortuner","Corolla","Mahindra":["Thar","Scorpio"]]]
        if company in d:
            print(d[company])
            print([Thar,Scorpio])
    def price(self,company,model):
        prunt("Yoy Have Selected",model)
        price_list={"Fortuner":4000000,"Corolla":3000000,"Thar":2900000,"Scorpio":3600000}
        if model in price_list:
            car_price=price_list[model]
            cgst=0.2*car_price
            sgst=0.1*car_price
            insurance=100000
            final_price=car_price+cgst+sgst+insurence
            print("On Road Price of the vehicle is :",final_price)
        