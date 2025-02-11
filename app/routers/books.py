from fastapi import APIRouter, HTTPException
from app.models import Book
from app.database import books_db

router = APIRouter()

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Get a book by its ID"""
    book = next((book for book in books_db if book["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book