#oop pragram to select a vehicle and display the price and change if required
class vehicle:
    def __init__(self, car, minivan, jeep):
        self.car = car
        self.minivan = minivan
        self.jeep = jeep
    def change(self, car, minivan, jeep):
        self.car = car
        self.minivan = minivan
        self.jeep = jeep


v = vehicle(10000, 15000, 20000)
print(v.car)



