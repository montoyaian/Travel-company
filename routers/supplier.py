from Classes.supplier import Supplier
from controller.db_controller_supplier import DatabaseControllerSupplier
from fastapi import APIRouter, Depends, HTTPException
from models.supplier_model import *

bd_object_supplier = DatabaseControllerSupplier() 

supplier_router = APIRouter(
    prefix="/supplier",
    tags=["Supplier"],
)

@supplier_router.post("/add/supplier")
async def add_supplier(supplier:Suppliermodel):
    """
    Add a offer to database
    """
    return bd_object_supplier.insert_supplier(Supplier(id=id, name=supplier.name, contact=supplier.contact,description=supplier.description))
        
@supplier_router.put("/edit/supplier/{supplier_id}")
async def edit_supplier(supplier_id, supplier : supplierUpdateModel):
    """
    edit supplier to database
    """
    return bd_object_supplier.edit_supplier(Supplier(id=supplier_id, name=supplier.name, contact=supplier.contact,description=supplier.description))


@supplier_router.delete("/delete/supplier/{id}")
def delete_supplier(id:int = 1):
    """
    delete a supplier to database
    """ 
    return bd_object_supplier.delete_supplier(id= id)

@supplier_router.get("/get/supplier/{id}")
def show_supplier(id:str = "all or id"):
    """
    show supplier
    """ 
    return bd_object_supplier.show_supplier(id=id)

@supplier_router.get("/get/suppliername")
def show_supplier_name():
    """
    show supplier name
    """ 
    return bd_object_supplier.show_supplier_name()