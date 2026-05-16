from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.core.database import get_session
from app.models.group import GroupRead, GroupCreate
from app.models.student import StudentRead
from app.services.group_service import GroupService
from app.services.student_service import StudentService

router = APIRouter()

@router.post("/", response_model=GroupRead, status_code=status.HTTP_201_CREATED)
def create_group(group_in: GroupCreate, session: Session = Depends(get_session)):
    return GroupService.create_group(session, group_in)

@router.get("/{id}", response_model=GroupRead)
def get_group(id: int, session: Session = Depends(get_session)):
    group = GroupService.get_by_id(session, id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

@router.get("/", response_model=List[GroupRead])
def get_groups(session: Session = Depends(get_session)):
    return GroupService.get_all(session)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_group(id: int, session: Session = Depends(get_session)):
    if not GroupService.delete_group(session, id):
        raise HTTPException(status_code=404, detail="Group not found")

@router.post("/{group_id}/students/{student_id}", response_model=StudentRead)
def add_student_to_group(group_id: int, student_id: int, session: Session = Depends(get_session)):
    return StudentService.add_to_group(session, student_id, group_id)

@router.delete("/{group_id}/students/{student_id}", response_model=StudentRead)
def remove_student_from_group(group_id: int, student_id: int, session: Session = Depends(get_session)):
    # Для удаления группы достаточно обнулить group_id у студента
    return StudentService.remove_from_group(session, student_id)

@router.get("/{group_id}/students", response_model=List[StudentRead])
def get_all_students_in_group(group_id: int, session: Session = Depends(get_session)):
    return StudentService.get_students_by_group(session, group_id)