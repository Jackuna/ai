from pydantic import BaseModel, Field, ValidationError

class Duck(BaseModel):
    name: str
    age: int = Field(gt=0)
    feather_count: int | None = Field(default=None, ge=0)

# Correct initialization
try:
    duck = Duck(name="Donald", age=5, feather_count=3000)
    print(duck)  # Duck(name='Donald', age=5, feather_count=3000)
except ValidationError as e:
    print(f"Validation Error:\n{e}")

# Faulty initialization
try:
    invalid_duck = Duck(name="Daffy", age=0, feather_count=-1)
    print(invalid_duck)
except ValidationError as e:
    print(f"Validation Error:\n{e}")