## Static Methods: A method that belong to a class rather than any object from that class (instance).
        # Usually used for general utility functions

## Instance Methods = Best for operations on instances of the class (object).


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    

print(Employee.is_valid_position("Associate"))

print(Employee.is_valid_position("Manager"))

employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())