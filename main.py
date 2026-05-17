import os
import uvicorn
from fastapi import FastAPI
from app.core.database import init_db
from app.api.routers import api_router

app = FastAPI(title="Student Management API", version="1.0.0")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(api_router)

if __name__ == "__main__":
    # Считываем переменные, задавая значения по умолчанию на случай их отсутствия
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", 8000))
    
    # Переводим строковое значение из .env в булево (True/False)
    reload = os.getenv("APP_RELOAD", "True").lower() in ("true", "1", "yes")

    uvicorn.run("main:app", host=host, port=port, reload=reload)