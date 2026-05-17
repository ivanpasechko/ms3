from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.student import Student, StudentCreate

class StudentService:
    @staticmethod
    def create_student(session: Session, student_in: StudentCreate) -> Student:
        db_student = Student.model_validate(student_in)
        session.add(db_student)
        session.commit()
        session.refresh(db_student)
        return db_student

    @staticmethod
    def get_by_id(session: Session, student_id: int) -> Optional[Student]:
        return session.get(Student, student_id)

    @staticmethod
    def get_all(session: Session) -> List[Student]:
        return session.exec(select(Student)).all()

    @staticmethod
    def delete_student(session: Session, student_id: int) -> bool:
        student = session.get(Student, student_id)
        if not student:
            return False
        session.delete(student)
        session.commit()
        return True

    @staticmethod
    def add_to_group(session: Session, student_id: int, group_id: int) -> Student:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        student.group_id = group_id
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

    @staticmethod
    def remove_from_group(session: Session, student_id: int) -> Student:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        student.group_id = None
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

    @staticmethod
    def get_students_by_group(session: Session, group_id: int) -> List[Student]:
        return session.exec(select(Student).where(Student.group_id == group_id)).all()

    @staticmethod
    def transfer_student(session: Session, student_id: int, from_group_id: int, to_group_id: int) -> Student:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        if student.group_id != from_group_id:
            raise HTTPException(status_code=400, detail="Student is not in specified Group A")
        
        student.group_id = to_group_id
        session.add(student)
        session.commit()
        session.refresh(student)
        return student