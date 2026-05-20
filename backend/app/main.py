from fastapi import FastAPI

from app.database.db import engine
from app.database.db import Base
from fastapi.middleware.cors import CORSMiddleware
from app.models.interaction_model import Interaction

from app.routes.interaction_routes import router as interaction_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CREATE DATABASE TABLES
Base.metadata.create_all(bind=engine)


# REGISTER ROUTES
app.include_router(interaction_router)


# ROOT ROUTE
@app.get("/")
def home():

    return {
        "message": "AI CRM Backend Running"
    }