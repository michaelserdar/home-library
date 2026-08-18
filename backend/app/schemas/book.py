from pydantic import BaseModel, Field

# class contains the common fields for creating and updating a book, as well as the response model for returning book data
class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    author: str = Field(min_length=1, max_length=255)
    isbn: str | None = Field(default=None, max_length=20)
    publication_year: int | None = None
    pages: int | None = None
    genre: str | None = Field(default=None, max_length=100)
    reading_status: str = "unread"
    rating: int | None = Field(default=None, ge=1, le=5)
    notes: str | None = None

# class contains the fields for creating a new book, inheriting from BookBase
class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int 

    model_config = {
        "from_attributes": True
    }
