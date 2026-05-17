from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.core.database import get_session
from app.models.student import StudentRead, StudentCreate
from app.services.student_service import StudentService

router = APIRouter()

@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(student_in: StudentCreate, session: Session = Depends(get_session)):
    return StudentService.create_student(session, student_in)

@router.get("/{id}", response_model=StudentRead)
def get_student(id: int, session: Session = Depends(get_session)):
    student = StudentService.get_by_id(session, id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/", response_model=List[StudentRead])
def get_students(session: Session = Depends(get_session)):
    return StudentService.get_all(session)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: int, session: Session = Depends(get_session)):
    if not StudentService.delete_student(session, id):
        raise HTTPException(status_code=404, detail="Student not found")

@router.post("/{student_id}/transfer", response_model=StudentRead)
def transfer_student(student_id: int, from_group: int, to_group: int, session: Session = Depends(get_session)):
    return StudentService.transfer_student(session, student_id, from_group, to_group)