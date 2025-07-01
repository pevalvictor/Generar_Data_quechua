from fastapi import FastAPI
from app.routes import router
from fastapi.staticfiles import StaticFiles

from app import models
from app.database import Base, engine
app = FastAPI()
app.include_router(router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")



# Esto creará las tablas si no existen
Base.metadata.create_all(bind=engine)
