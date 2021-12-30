#oop pragram to select a vehicle and display the price and change if required
class vehicle:
    def __init__(self, car, minivan, jeep):
        self.car = car
        self.minivan = minivan
        self.jeep = jeep
        
v = vehicle(10000, 15000, 20000)

vehi = input("Enter the type of vehicle you would like to buy: ")
if vehi == "car":
    print(v.car)
elif vehi == "minivan":
    print(v.minivan)
elif vehi == "jeep":
    print(v.jeep)
else:
    print("ERROR")

opt = input("would you like to change your decision? ")
if opt == "yes":
    done_choosing = False
elif opt == "no":
    done_choosing = True

while done_choosing == False:
    vehi = input("Enter the type of vehicle you would like to buy: ")
    if vehi == "car":
        print(v.car)
        opt = input("would you like to change your decision? ")
        if opt == "yes":
            done_choosing == False
        elif opt == "no":
            done_choosing == True
    elif vehi == "minivan":
        print(v.minivan)
        opt = input("would you like to change your decision? ")
        if opt == "yes":
            done_choosing == False
        elif opt == "no":
            done_choosing == True
    elif vehi == "jeep":
        print(v.jeep)
        opt = input("would you like to change your decision? ")
        if opt == "yes":
            done_choosing == False
        elif opt == "no":
            done_choosing == True
    else:
        print("ERROR")

if opt == "no":
    print("You have officially chosen your vehicle")






    








    





