from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, WebSocket, Request, Depends
import asyncio
from sqlalchemy.orm import Session
from database import get_db
import models
from database import engine

from api_data_manager import get_all_records
from helperfuncs import send_data_to_frontend

app = FastAPI()
templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def home(request: Request):
    """Display live data from Mandrill API"""
    return templates.TemplateResponse("home.html", {"request": request})

@app.websocket("/ws/mandrill/broadcast")
async def websocket_endpoint(websocket: WebSocket, db: Session=Depends(get_db)):
    """Display live data from Mandrill API"""
    await send_data_to_frontend(websocket, db)

@app.get("/dashboard")
def dashboard(request: Request, db: Session=Depends(get_db)):
    """Display all data saved in the database"""
    data = get_all_records(db)
    print(data)
    return templates.TemplateResponse("dashboard.html", {"request" : request, "data": data})