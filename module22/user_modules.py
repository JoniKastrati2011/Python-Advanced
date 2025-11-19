from pydantic import BaseModel, conint, constr
from typing import Optional
class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

#validation

user = User(id=1, name="John", age=30, email="john@example.com")

#default values and optimal fields
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

user1 = User(id=1, name="John", age=30, email="john@example.com")
print(user1)

user2 = User(id=2, name="John Doe",email="")
print(user2)

user3 = User(id=3, name="John Doe")
print(user3)

user4 = User(id=4, name="John Doe", age=None)
print(user4)

#field constraints

class another_user(BaseModel):
    id: coint(gt=0)
    name: constr(min_length=1, max_length=100)

valid_user = another_user(id=1, name='Alice')
print(valid_user)

invalid_user = another_user(id=2, name='Alice')
print(invalid_user)