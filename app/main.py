from datetime import date
from typing import Optional
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

app = FastAPI()

class SGetHotels():
    def __init__(
        self,
        location,
        date_from,
        date_to,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, qe=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

@app.get("/hotel/{location}")
def get_hotels(
    hotels_arg: SGetHotels = Depends(),
):
    return hotels_arg

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
    
class SHotelPost(BaseModel):
    address: str
    has_spa: bool
    stars: int

@app.post("/booking")
def add_booking(
    booking: SBooking,
) -> list[SHotelPost]:
    hotels = [
        {
            "address": "Ул. Гоголя, д.1",
            "has_spa": True,
            "stars": 5,
        }
    ]
    return hotels