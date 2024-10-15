from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models import Person, Room
from db import get_db, DBOperations

class BuildingController:
    @staticmethod
    def get_all_rooms(db: Session = Depends(get_db)):
        db_rooms = DBOperations.get_all_rooms(db)
        return [Room(id=room.id, name=room.name, occupants=[Person(id=p.id, name=p.name) for p in room.occupants]) for room in db_rooms]

    @staticmethod
    def get_room(room_id: int, db: Session = Depends(get_db)):
        db_room = DBOperations.get_room(db, room_id)
        if not db_room:
            raise HTTPException(status_code=404, detail="Room not found")
        return Room(id=db_room.id, name=db_room.name, occupants=[Person(id=p.id, name=p.name) for p in db_room.occupants])

    @staticmethod
    def add_room(room: Room, db: Session = Depends(get_db)):
        db_room = DBOperations.create_room(db, room)
        return Room(id=db_room.id, name=db_room.name, occupants=[])

    @staticmethod
    def add_person_to_room(room_id: int, person: Person, db: Session = Depends(get_db)):
        db_person = DBOperations.add_person_to_room(db, room_id, person)
        db_room = DBOperations.get_room(db, room_id)
        return Room(id=db_room.id, name=db_room.name, occupants=[Person(id=p.id, name=p.name) for p in db_room.occupants])
