from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    name: str

class Author(AuthorBase):
    id: int