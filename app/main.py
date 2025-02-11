from fastapi import FastAPI
from app.routers import books

app = FastAPI(
    title="Book API",
    description="A simple API for managing books",
    version="1.0.0"
)

app.include_router(books.router, prefix="/api/v1/books", tags=["books"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Book API"}