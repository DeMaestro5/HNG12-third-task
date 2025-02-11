from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import books

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the books router with the correct prefix
app.include_router(books.router, prefix="/api/v1/books", tags=["books"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Book API. Use /api/v1/books/{book_id} to get book details"}