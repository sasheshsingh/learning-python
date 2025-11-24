# Object = A bundle of related attributes (variables) and methods (functions).
# Ex. Phone, Cup, Book

# Class = (Blueprint) used to design the structure of an object.

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You Drive the {self.model}.")

    def stop(self):
        print(f"You stop the {self.model}")
    
    def describe(self):
        print(f"{self.model} {self.year} {self.color} {self.for_sale}")


