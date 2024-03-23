def page():
    # n=1
    # while n!=0:
    while True:
        username=input("Enter Username:")
        password=input("Enter Password:")
            
        if (username==password):
            print("Succefully logged in")
            break
        else:
            print("Re Enter The details")
page()
