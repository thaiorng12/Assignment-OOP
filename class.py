class Dog :
    def __init__(self,Name,Size):
        self.name=Name
        self.size=Size
    def bark(self):
        print("Dog is barking")
    def eat(self):
        print("Dog can eat")
wolf=Dog("Wolf","15inches")
print(wolf.name)
wolf.eat()