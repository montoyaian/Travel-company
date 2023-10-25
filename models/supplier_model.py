from typing import Optional

from pydantic import BaseModel


class Suppliermodel (BaseModel):
    name:Optional[str]
    contact:Optional[int]
    description:Optional[str]
    class Config:
        from_attributes = True


class supplierUpdateModel (Suppliermodel):
    id : Optional[int]
    class Config:
        from_attributes = True