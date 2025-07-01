from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib.parse

password = urllib.parse.quote_plus("73461697")
DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/traducciones"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
