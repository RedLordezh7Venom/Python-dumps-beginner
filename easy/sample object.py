class Car:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def myfunc(self):
        print("Hello my name is " + self.name)
p1=Car("Lamborghini",1943)
print(p1.name)
print(p1.year)
p1.myfunc()