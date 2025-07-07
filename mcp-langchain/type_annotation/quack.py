# Code snippet from - https://www.speakeasy.com/blog/pydantic-vs-dataclasses

class Duck:
    def quack(self):
        print("Quack!")

class Mallard:
    def quack(self):
        print("Quack!")

def make_duck_quack(duck):
    duck.quack()

make_duck_quack(Duck()) # prints "Quack!"
make_duck_quack(Mallard()) # prints "Quack!"