
from app.bookings.models import Bookings
from app.dao.base import BaseDao

class BookingsDao(BaseDao):
    model = Bookings