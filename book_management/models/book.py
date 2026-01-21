from pydantic import BaseModel
from typing import List, Optional

class BookBase(BaseModel):
    title: str
    author_id: int
    book_link: str
    genre: List[str]
    average_rating: Optional[float] = None
    published: Optional[int] = None

class BookCreate(BookBase):
        pass

class BookResponse(BookBase):
        pass

class Book(BookBase):
        id: int