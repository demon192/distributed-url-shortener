from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings


# DATABASE_URL = "postgresql://postgres:password@localhost/urlshort"

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()