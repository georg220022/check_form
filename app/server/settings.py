from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI, APIRouter
from .routes import routes


mongo_url = "mongodb://gera:gera@mongodb:27017"
client = AsyncIOMotorClient(mongo_url)

app = FastAPI()
app.state.mongo_client = client
app.include_router(APIRouter(routes=routes))
