from fastapi import APIRouter
from app.api.endpoints.students import router as students_router
from app.api.endpoints.groups import router as groups_router

api_router = APIRouter()
api_router.include_router(students_router, prefix="/students", tags=["students"])
api_router.include_router(groups_router, prefix="/groups", tags=["groups"])