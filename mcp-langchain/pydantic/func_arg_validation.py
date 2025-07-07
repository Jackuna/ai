from pydantic import BaseModel, Field, validate_call

class DuckDescription(BaseModel):
    name: str
    age: int = Field(gt=0)
    feather_count: int = Field(gt=0)

@validate_call
def describe_duck(duck: DuckDescription) -> str:
    return f"{duck.name} is {duck.age} years old and has {duck.feather_count} feathers."

# Valid input
print(describe_duck(DuckDescription(name="Donald", age=5, feather_count=3000)))
# Output: Donald is 5 years old and has 3000 feathers.

# Invalid input
try:
    print(describe_duck(DuckDescription(name="Daffy", age=0, feather_count=-1)))
except ValueError as e:
    print(f"Validation Error: {e}")
# Validation Error: 2 validation errors for DuckDescription
# age
#   Input should be greater than 0 [type=greater_than, input_value=0, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.8/v/greater_than
# feather_count
#   Input should be greater than 0 [type=greater_than, input_value=-1, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.8/v/greater_than