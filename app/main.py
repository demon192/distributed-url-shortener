from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import shorten, redirect
from app.config import settings
from app.database import Base, engine

app = FastAPI(title=settings.APP_NAME)


# CORS configuration (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create tables
Base.metadata.create_all(bind=engine)


# Register routes
app.include_router(shorten.router, tags=["Shorten"])
app.include_router(redirect.router, tags=["Redirect"])


@app.get("/")
def root():
    return {"message": "URL Shortener Service Running"}