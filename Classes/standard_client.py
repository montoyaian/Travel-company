from Classes.client import Client

class Standardclient(Client):
    def __init__(self, id:int, name:str, contact:int,bookings:int ,email:str,password:str):
        super().__init__(id, name, contact,bookings,email,password)
         
    def __str__(self):
        return {"id": self.id,
                "name": self.name,
                "contact": self.contact,
                "bookings": self.bookings,
                "email": self.email}