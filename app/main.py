from fastapi import FastAPI

from app.authentication.router import router as authentication_router
from app.files_app.router import router as files_router

app = FastAPI()
app.include_router(authentication_router, prefix='/auth')
app.include_router(files_router, prefix='/files')
