from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class DBPerson(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))

class DBRoom(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    occupants = relationship("DBPerson", back_populates="room")

DBPerson.room = relationship("DBRoom", back_populates="occupants")

# Create SQLite engine
engine = create_engine("sqlite:///./data/rooms.db", connect_args={"check_same_thread": False})

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DBOperations:
    @staticmethod
    def get_all_rooms(db):
        return db.query(DBRoom).all()

    @staticmethod
    def get_room(db, room_id):
        return db.query(DBRoom).filter(DBRoom.id == room_id).first()

    @staticmethod
    def create_room(db, room):
        db_room = DBRoom(id=room.id, name=room.name)
        db.add(db_room)
        db.commit()
        db.refresh(db_room)
        return db_room

    @staticmethod
    def add_person_to_room(db, room_id, person):
        db_person = DBPerson(id=person.id, name=person.name, room_id=room_id)
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return db_person