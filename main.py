from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from models import BookingsResponse
from data import movies_data  # Import the movies_data

app = FastAPI()


class BookingRequest(BaseModel):
    movie_id: int
    show_date: str
    show_time: str
    seat_type: str
    count: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1/bookings", response_model=BookingsResponse)
def get_bookings():
    return movies_data


@app.post("/v1/bookings", response_model=BookingsResponse)
def book_movie(req: BookingRequest):
    for movie in movies_data["movies"]:
        if movie["id"] == req.movie_id:
            for show in movie["shows"]:
                if show["date"] == req.show_date and show["time"] == req.show_time:
                    seat_types = show["seats"]["types"]
                    if req.seat_type in seat_types:
                        if seat_types[req.seat_type]["available"] >= req.count:
                            seat_types[req.seat_type]["available"] -= req.count
                            show["seats"]["available"] -= req.count
                            return movies_data
                        else:
                            raise HTTPException(
                                status_code=400, detail="Not enough seats available")
                    else:
                        raise HTTPException(
                            status_code=404, detail="Seat type not found")
            raise HTTPException(status_code=404, detail="Show not found")
    raise HTTPException(status_code=404, detail="Movie not found")
