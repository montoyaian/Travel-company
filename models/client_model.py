from typing import Optional

from pydantic import BaseModel


class ClientModel (BaseModel):
    name: Optional[str]
    contact: Optional[int]
    email: Optional[str]
    password: Optional[str]
    
class loginModel(BaseModel):
    name : Optional[str]
    password: Optional[str]