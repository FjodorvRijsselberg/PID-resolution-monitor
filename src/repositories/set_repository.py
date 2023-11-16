from sqlalchemy.orm import Session

from database import get_db
from models import PIDSet


class PIDSetRepository:
    """
    Initialize the PIDSetRepository.

    This class provides CRUD operations for the PIDSet model.
    """
    def __init__(self) -> None:
        self.session: Session = get_db().__next__()

    def create_pid_set(self, set_identifier: str) -> PIDSet:
        pid_set = PIDSet(set_identifier=set_identifier)
        self.session.add(pid_set)
        self.session.commit()
        self.session.refresh(pid_set)
        return pid_set

    def get_pid_set(self, set_id: int) -> PIDSet:
        return self.session.query(PIDSet).filter(
            PIDSet.set_id == set_id).first()

    def get_all_pid_sets(self) -> list[PIDSet]:
        return self.session.query(PIDSet).all()

    def delete_pid_set(self, set_id: int) -> bool:
        pid_set = self.get_pid_set(set_id)
        if pid_set:
            self.session.delete(pid_set)
            self.session.commit()
            return True
        return False
