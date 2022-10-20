from http.client import OK
from fastapi import FastAPI, Depends
from .schemas import CreateJobRequest
from sqlalchemy.orm import Session
from .database import get_db
from .models import Job

app = FastAPI()
@app.post("/")
def create(details: CreateJobRequest, db: Session = Depends(get_db)):
    to_create = Job(
        title= details.title,
        description=details.description
    )
    db.add(to_create)
    db.commit()
    return{
        "success": True,
        "created_id": to_create.id
    }

@app.get("/")
def get(db: Session = Depends(get_db)):
    return db.query(Job).all()

@app.get("/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.id == id).first()

@app.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Job).filter(Job.id == id).delete()
    db.commit()
    return {"success": True}