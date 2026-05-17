from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class GroupBase(SQLModel):
    name: str = Field(index=True, unique=True)

class Group(GroupBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    students: List["Student"] = Relationship(back_populates="group")

class GroupCreate(GroupBase):
    pass

class GroupRead(GroupBase):
    id: int