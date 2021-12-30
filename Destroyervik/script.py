# OOP  program that has methods; reverse an array, find an element, bubble sort.

class profile:

    def __init__(self, name, age, sub):
        self.name = name
        self.age = age
        self.sub = sub

    def change(self, name, age, sub):
        self.name = name
        self.age = age
        self.sub = sub


d = profile('Elon', 35, 'physics')

print(d.name, d.age, d.sub)

d.change('Mark', 37, 'Facebook')
print(d.name, d.age, d.sub)
