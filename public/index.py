from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.routes import define_routes
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
define_routes(app)
