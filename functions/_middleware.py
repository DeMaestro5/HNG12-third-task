# functions/_middleware.py
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

def onRequest(context):
    return app(context["request"])