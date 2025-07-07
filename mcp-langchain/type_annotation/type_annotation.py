# Code snippet from - https://www.speakeasy.com/blog/pydantic-vs-dataclasses
# Type annotations were introduced in Python 3.5

class Duck:
    def quack(self):
        print("Quack!")


class RubberDuck:
    def quack(self):
        print("Quack!")


def make_duck_quack(duck: Duck):
    duck.quack()

make_duck_quack(Duck()) # prints "Quack!"
make_duck_quack(RubberDuck())
# Pylance will show the hint: Argument 1 to "make_duck_quack" has incompatible type "RubberDuck"; expected "Duck".