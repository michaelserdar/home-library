from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.connection import engine 
from app.models.book import Book 
from app.schemas.book import BookCreate, BookResponse 

router = APIRouter(
    prefix="/api/books",
    tags=["books"],
)

def get_db():
    with Session(engine) as session:
        yield session

@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    statement = select(Book).order_by(Book.id)
    books = db.scalars(statement).all()
    return books

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return book

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(book_data: BookCreate, db: Session = Depends(get_db)):
    book = Book(**book_data.model_dump())

    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookCreate, db: Session = Depends(get_db),):
    book = db.get(Book, book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found",)

    for field, value in book_data.model_dump().items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)

    return book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found",)

    db.delete(book)
    db.commit() 


    
    
