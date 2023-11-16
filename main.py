from fastapi import Depends, FastAPI, Response, status  
from starlette.middleware.cors import CORSMiddleware
from routers.clients import client_router
from routers.supplier import supplier_router
from routers.offers import offers_router
from routers.fligh import flight_router
from routers.booking import bookings_router
from models.client_model import *
from controller.db_controller_clients import DatabaseControllerClient

app = FastAPI(title="Travel company API")
bd_object_client = DatabaseControllerClient() 
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(client_router)
app.include_router(bookings_router)
app.include_router(offers_router)
app.include_router(flight_router)
app.include_router(supplier_router)


@app.get("/")
async def root():
    return {"Hello": "Travel company API"}

@app.post("/login")
async def login(data : loginModel):
    """
    Login app
    """
    return bd_object_client.login(data)



