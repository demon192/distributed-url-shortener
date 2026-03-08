from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.url import URL
from app.services.hash_service import encode

router = APIRouter()

@router.post("/shorten")
def shorten_url(url: str):

    db: Session = SessionLocal()

    new = URL(long_url=url)
    db.add(new)
    db.commit()
    db.refresh(new)

    short_code = encode(new.id)

    new.short_code = short_code
    db.commit()

    return {"short_url": f"http://localhost:8000/{short_code}"}