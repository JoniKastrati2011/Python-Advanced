from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

class Person(BaseModel):
    name: str
    age: int

@app.post("/users/")
async def create_user(user: User):
    return user

@app.post("/create_peron")
async def create_peron(person: Person):
    return {"message": f"Person{person.name} created successfully{person.age}"}