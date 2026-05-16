from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class StudentBase(SQLModel):
    full_name: str
    age: int
    gpa: float
    group_id: Optional[int] = Field(default=None, foreign_key="group.id")

class Student(StudentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    group: Optional["Group"] = Relationship(back_populates="students")

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int