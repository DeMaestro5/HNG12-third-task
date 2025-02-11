from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import books_db
from app.routers import books

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the books router
app.include_router(books.router, prefix="/books", tags=["books"])

@app.get("/")
async def root():
    """Return all books in the database"""
    return {
        "books": books_db
    }