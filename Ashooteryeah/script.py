#oop pragram that has methods :reverse an array,find an element, bubble sort

class profile:

    def __init__(self, name, age, sub):
        self.name = name
        self.age = age
        self.sub = sub
    def change(self, name, age, sub):
        self.name = name
        self.age = age
        self.sub = sub


d = profile("steve",51,"apple")
print(d.name,d.age,d.sub)

d.change("mark",45,"meta")
print(d.name,d.age,d.sub)



