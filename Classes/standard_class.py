from Classes.flight import Flight
from datetime import date,time

class Standardclass(Flight):
    def __init__(self, id:int, origin:str, destination:str, date:date, positions:int, hour:time, id_agency:int, standard_cost:float):
        super().__init__(id, origin, destination, date, positions, hour, id_agency)
        self.__standard_cost = standard_cost
        
    @property
    def standard_cost(self):
        return self.__standard_cost
    @standard_cost.setter
    def standard_cost(self, new_standard_cost):
        self.__standard_cost = new_standard_cost
        
    def __str__(self):
        return {"id": self.id,
                "origin": self.origin,
                "destination": self.destination,
                "date": self.date,
                "positions": self.positions,
                "hour": self.hour,
                "id_agency": self.id_agency,
                "standard_cost": self.__standard_cost}