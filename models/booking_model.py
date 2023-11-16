from typing import Optional

from pydantic import BaseModel


class Bookingmodel (BaseModel):
    cant_positions:Optional[int]
    id_client:Optional[int]
    type_client:Optional[str]
    class Config:
        from_attributes = True



class BookingUpdateModel (BaseModel):
    cant_positions:Optional[int]
    class Config:
        from_attributes = True

class Billmodel (BaseModel):
    payment_method: Optional[str]
    class Config:
        from_attributes = True