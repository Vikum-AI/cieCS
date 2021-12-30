# Data on model and price
vehicles = ['car', 'minivan', 'jeep']
price = [10000, 15000, 20000]


class buy:

    # Selecting a model and displaying price
    def __init__(self, model):

        self.model = model.lower()
        self.n = len(vehicles)

        for i in range(self.n):
            if self.model == vehicles[i]:
                self.price = price[i]
                break

        print("You have chosen a", self.model)
        print("Which costs", self.price)

    def change(self, model):
        self.model = model.lower()
        self.n = len(vehicles)

        for i in range(self.n):
            if self.model == vehicles[i]:
                self.price = price[i]
                break

        print("You have changed to a", self.model)
        print("Which costs", self.price)


d = buy('car')
d.change('jeep')
d.change('minivan')








