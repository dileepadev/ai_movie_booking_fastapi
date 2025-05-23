from pydantic import BaseModel
from typing import List, Dict


class SeatType(BaseModel):
    available: int
    price: float


class Seats(BaseModel):
    total: int
    available: int
    types: Dict[str, SeatType]


class Show(BaseModel):
    date: str
    time: str
    hall: str
    seats: Seats


class Movie(BaseModel):
    id: int
    title: str
    language: str
    cinema: str
    shows: List[Show]


class BookingsResponse(BaseModel):
    movies: List[Movie]
