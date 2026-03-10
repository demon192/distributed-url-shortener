# from app.services.cache_service import check_rate_limit
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.url import URL

router = APIRouter()

@router.get("/{code}")
def redirect(code: str):

    db: Session = SessionLocal()

    url = db.query(URL).filter(URL.short_code == code).first()

    if not url:
        return {"error": "URL not found"}

    url.click_count += 1
    db.commit()

    # if not check_rate_limit(url.client_ip):
    #     return {"error": "Too many requests"}

    return RedirectResponse(url.long_url)