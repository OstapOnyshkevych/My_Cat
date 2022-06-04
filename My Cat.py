class Animal:                                   #Клас тварин
    def __init__(self, Animal):
        print(Animal, 'is an animal.')
    def name(self):
        print("Name of my cat is Jessie.")

class Mammal(Animal):                           #Клас ссавців
    def __init__(self, Name):
        print(Name, 'is a warm-blooded animal.')
        super().__init__(Name)
    def color(self):
        print("My cat is black.")
    def teeth(self):
        print("Jessie has got sharp teeth.")

class Fly(Mammal):                              #Клас літаючих ссавців
    def __init__(self, Fly):
        print(Fly, "can't fly.")
        super().__init__(Fly)

class Swim(Mammal):                             #Клас плаваючих ссавців
    def __init__(self, Swim):
        print(Swim, "can swim.")
        super().__init__(Swim)
    def swim(self):
        print("She can swim very well.")

class Cat(Fly,Swim):                           #Клас котів
    def __init__(self):
        print('Cat has 4 legs.')
        super().__init__('Cat')
        super().name()
        super().color()
        super().teeth()
        super().swim()

cat = Cat()