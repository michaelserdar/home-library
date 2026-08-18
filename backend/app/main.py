from fastapi import FastAPI
from sqlalchemy import text

from app.api.books import router as books_router
from app.database.base import Base
from app.database.connection import engine 
from app.models.book import Book

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Home Library API",
    description="API for managing a home library",
    version="0.1.0",
)

app.include_router(books_router)

@app.get("/")
def root():
    return {"message": "Home Library API is running"}

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}                                    
