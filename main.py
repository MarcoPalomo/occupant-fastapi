from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from controllers import BuildingController
from models import Room, Person
from db import get_db
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/api/rooms")
async def get_rooms(db: Session = Depends(get_db)):
    return BuildingController.get_all_rooms(db)

@app.get("/api/rooms/{room_id}")
async def get_room(room_id: int, db: Session = Depends(get_db)):
    return BuildingController.get_room(room_id, db)

@app.post("/api/rooms")
async def create_room(room: Room, db: Session = Depends(get_db)):
    return BuildingController.add_room(room, db)

@app.post("/api/rooms/{room_id}/occupants")
async def add_occupant(room_id: int, person: Person, db: Session = Depends(get_db)):
    return BuildingController.add_person_to_room(room_id, person, db)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)