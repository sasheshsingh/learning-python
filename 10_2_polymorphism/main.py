# "Duck Typing"

# Another way to achieve polymorphism besides Inheritance.
# Object must have the minimum necessary attributes/methods.
# If it looks like a Duck and Quck like a duct, it must be Duck.


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("BARK!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car:
    alive = True
    def speak(self):
        print("HONK!")

animals = [Car(), Dog(), Car()]

for animal in animals:
    print(animal.alive)
    animal.speak()