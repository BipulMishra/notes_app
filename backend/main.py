from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import database, models, crud

# Create tables if they don't exist
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Notes API")

# Allow requests from Streamlit (frontend)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------
# READ ALL NOTES
# -------------------------------
@app.get("/notes")
def list_notes(db: Session = Depends(get_db)):
    notes = crud.get_notes(db)
    return notes

# -------------------------------
# READ ONE NOTE
# -------------------------------
@app.get("/notes/{note_id}")
def read_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

# -------------------------------
# CREATE NOTE
# -------------------------------
@app.post("/notes")
def create_new(title: str, content: str, db: Session = Depends(get_db)):
    if not title.strip() or not content.strip():
        raise HTTPException(status_code=400, detail="Title and content cannot be empty.")
    return crud.create_note(db, title, content)

# -------------------------------
# UPDATE NOTE
# -------------------------------
@app.put("/notes/{note_id}")
def update_existing(note_id: int, title: str, content: str, db: Session = Depends(get_db)):
    if not title.strip() or not content.strip():
        raise HTTPException(status_code=400, detail="Title and content cannot be empty.")
    updated_note = crud.update_note(db, note_id, title, content)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

# -------------------------------
# DELETE NOTE
# -------------------------------
@app.delete("/notes/{note_id}")
def delete_existing(note_id: int, db: Session = Depends(get_db)):
    deleted_note = crud.delete_note(db, note_id)
    if not deleted_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": f"Note with ID {note_id} deleted successfully"}
