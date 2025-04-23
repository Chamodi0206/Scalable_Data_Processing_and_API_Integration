from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base, User, Country
from fetch_users import fetch_and_store_users
from fetch_countries import fetch_and_store_countries
from logger import logger
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    db = next(get_db())
    logger.info("Starting up app and fetching data")
    fetch_and_store_users(db)
    fetch_and_store_countries(db)

@app.get("/")
def read_root():
    return {"message": "Data pipeline is running!"}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/countries")
def get_countries(db: Session = Depends(get_db)):
    return db.query(Country).all()

@app.get("/health")
def health_check():
    return {"status": "ok"} 
