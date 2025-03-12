from fastapi import FastAPI

from app.authentication_app.router import router as authentication_router
from app.files_app.router import router as files_router

app = FastAPI()
app.include_router(authentication_router)
app.include_router(files_router)
