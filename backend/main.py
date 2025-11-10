from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import database, models, crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Notes API")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/notes")
def list_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)

@app.post("/notes")
def create_new(title: str, content: str, db: Session = Depends(get_db)):
    return crud.create_note(db, title, content)

@app.delete("/notes/{note_id}")
def delete_existing(note_id: int, db: Session = Depends(get_db)):
    return crud.delete_note(db, note_id)
