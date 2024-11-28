from fastapi import APIRouter

from app.bookings.dao import BookingsDao
from app.bookings.shemas import SBooking


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingsDao.find_all()

        
@router.get("/{booking_id}")
async def get_booking(booking_id: int) -> SBooking:
    return await BookingsDao.find_by_id(booking_id)