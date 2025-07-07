from typing import Annotated

Age = Annotated[int, "type integer betweeen 1 to 100"]

def print_age(age: Age) -> None:
    print(age)

class Duck:
    def quack(self):
        print("Quack!")

class Mallard:
    def quack(self):
        print("Quack!")

def make_duck_quack(duck):
    duck.quack()

Duck().quack()
make_duck_quack(Duck()) # prints "Quack!"
make_duck_quack(Mallard()) # prints "Quack!"

from dataclasses import dataclass


@dataclass
class Duck:
    name: str
    age: int

    def quack(self):
        print(f"{self.name} says: Quack!")


donald = Duck("kunal", "myworld")
print(donald)  # Duck(name='Donald', age=5)
#donald.quack()  # Donald says: Quack!

#daffy = Duck("Daffy", "3")
# Pylance will show the hint: Argument of type "Literal['3']" cannot be assigned to parameter "age" of type "int" in function "__init__".
