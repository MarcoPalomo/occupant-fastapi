from pydantic import BaseModel
from typing import List #Dict

class Person(BaseModel):
    id: int
    name: str

class Room(BaseModel):
    id: int
    name: str
    occupants: List[Person] = []

# In-memory database
# db: Dict[int, Room] = {}
