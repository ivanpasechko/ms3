from typing import List, Optional
from sqlmodel import Session, select
from app.models.group import Group, GroupCreate

class GroupService:
    @staticmethod
    def create_group(session: Session, group_in: GroupCreate) -> Group:
        db_group = Group.model_validate(group_in)
        session.add(db_group)
        session.commit()
        session.refresh(db_group)
        return db_group

    @staticmethod
    def get_by_id(session: Session, group_id: int) -> Optional[Group]:
        return session.get(Group, group_id)

    @staticmethod
    def get_all(session: Session) -> List[Group]:
        return session.exec(select(Group)).all()

    @staticmethod
    def delete_group(session: Session, group_id: int) -> bool:
        group = session.get(Group, group_id)
        if not group:
            return False
        session.delete(group)
        session.commit()
        return True