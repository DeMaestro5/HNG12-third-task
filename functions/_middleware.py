from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.main import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def handle_request(request):
    return app(request)