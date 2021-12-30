# Data on model and price
vehicles = ['car', 'minivan', 'jeep']
price = [10000, 15000, 20000]


class vehicle:

    def __init__(self, model):
        self.model = model
        n = len(vehicles)

        for i in range(n):
            if model == vehicles[i]:
                self.price = price[i]
                break
        print(self.price)

    def change(self, model):
        self.model = model
        n = len(vehicles)

        for i in range(n):
            if model == vehicles[i]:
                self.price = price[i]
                break
        print(self.price)


d = vehicle('jeep')
d.change('car')
