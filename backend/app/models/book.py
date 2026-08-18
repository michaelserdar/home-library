from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column 

from app.database.base import Base

class Book(Base):
    __tablename__ = "books" 

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    isbn: Mapped[str | None] = mapped_column(String(20), unique=True, nullable=True)
    publication_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    pages: Mapped[int | None] = mapped_column(Integer, nullable=True)
    genre: Mapped[str | None] = mapped_column(String(100), nullable=True)
    reading_status: Mapped[str | None] = mapped_column(
        String(50), 
        nullable=False, 
        default="unread",
        )
    rating: Mapped[int | None] = mapped_column(Integer, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
