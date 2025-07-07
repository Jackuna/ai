# Code snippet from - https://www.speakeasy.com/blog/pydantic-vs-dataclasses
# Introduced in Python 3.7

from dataclasses import dataclass

@dataclass
class Duck:
    name: str
    age: int

    def quack(self):
        print(f"{self.name} says: Quack!")


donald = Duck("Donald", 5)
mickey = Duck("Mickey",7)
print(donald,mickey)  # Duck(name='Donald', age=5)
donald.quack()  # Donald says: Quack!
mickey.quack()

mini = Duck("Mini","3")
# Pylance will show the hint: Argument of type "Literal['3']" cannot be assigned to parameter "age" of type "int" in function "__init__".