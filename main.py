from fastapi import FastAPI
from app.core.database import init_db
from app.api.routers import api_router

app = FastAPI(title="Student Management API", version="1.0.0")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.py:app", host="0.0.0.0", port=8000, reload=True)