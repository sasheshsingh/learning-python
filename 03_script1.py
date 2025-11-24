from script2 import *

print(dir("__name__"))

# Dunder Functions
# Good Practise(Code is modular, helps readability, leaves no global variables, avoid unintended execution)
print(__name__)


def favourite_food(food):
    print(f"Your favourite food is {food}!")

def main():
    print("This is script1.")
    favourite_food("Pizza")
    print("GoodBye!")

if __name__ == "__main__":
    main()