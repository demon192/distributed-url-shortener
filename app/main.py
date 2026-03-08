from fastapi import FastAPI
from app.routes import shorten, redirect
from app.config import settings
from app.database import Base, engine

app = FastAPI(title=settings.APP_NAME)


# Create tables
Base.metadata.create_all(bind=engine)


# Register routes
app.include_router(shorten.router, tags=["Shorten"])
app.include_router(redirect.router, tags=["Redirect"])


@app.get("/")
def root():
    return {"message": "URL Shortener Service Running"}