from models.client_model import *


class Standard_clientmodel (ClientModel):

    class Config:
        from_attributes = True


class Standard_clientUpdateModel (ClientModel):
    
    class Config:
        from_attributes = True