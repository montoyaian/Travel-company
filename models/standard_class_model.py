from models.flight_model import *
from typing import Optional

class standard_flight_model (FlightModel):
    standard_cost :  Optional[float]
    class Config:
        from_attributes = True



class fly_standard_UpdateModel (standard_flight_model):
    class Config:
        from_attributes = True