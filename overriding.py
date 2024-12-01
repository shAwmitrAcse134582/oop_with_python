class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    
    def eat(self):
        print('I love biriyani')



class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team=team
        super().__init__(name, age, height, weight)

    def eat(self):
        print('You should mantain diet chart')

sakib=Cricketer('sakib',35,70,85,'BD')
sakib.eat()
