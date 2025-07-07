# Code snippet from - https://www.speakeasy.com/blog/pydantic-vs-dataclasses
# TypeDict were introduced in Python 3.8

from typing import TypedDict


class DuckStats(TypedDict):
    name: str
    age: int
    feather_count: int


def describe_duck(stats: DuckStats) -> str:
    return f"{stats['name']} is {stats['age']} years old and has {stats['feather_count']} feathers."


print(
    describe_duck(
        {
            "name": "Donald",
            "age": 5,
            "feather_count": 3000,
        }
    )
)
# Output: Donald is 5 years old and has 3000 feathers.

print(
    describe_duck(
        {
            "name": "Daffy",
            "age": "3",  # Pylance will show the hint: Argument of type "Literal['3']" cannot be assigned to parameter "age" of type "int" in function "describe_duck"
            "feather_count": 5000,
        }
    )
)