from datetime import datetime
from sqlalchemy.orm import Session

from database import get_db
from models import MonitorSession


class MonitorSessionRepository:
    """
    Initialize the MonitorSessionRepository.

    This class provides CRUD operations for the MonitorSession model.
    """

    def __init__(self) -> None:
        self.session: Session = get_db().__next__()

    def create_monitor_session(self, set_id: int) -> MonitorSession:
        start_time = datetime.now()
        monitor_session = MonitorSession(
            start_time=start_time,
            end_time=None,
            set_id=set_id
        )
        self.session.add(monitor_session)
        self.session.commit()
        self.session.refresh(monitor_session)
        return monitor_session

    def get_monitor_session(self, monitor_session_id: int) -> MonitorSession:
        return self.session.query(MonitorSession).filter(
            MonitorSession.id == monitor_session_id).first()

    def get_all_monitor_sessions(self) -> list[MonitorSession]:
        return self.session.query(MonitorSession).all()

    def get_monitor_sessions_for_pid_set(self, pid_set_id: int) -> list[
         MonitorSession]:
        return self.session.query(MonitorSession).filter(
            MonitorSession.set_id == pid_set_id).all()

    def update_end_time(self, end_time: datetime,
                        monitor_session_id) -> MonitorSession:
        monitor_session = self.get_monitor_session(monitor_session_id)
        if monitor_session:
            monitor_session.end_time = end_time
            self.session.commit()
            self.session.refresh(monitor_session)
        return monitor_session

    def delete_monitor_session(self, monitor_session_id: int) -> bool:
        monitor_session = self.get_monitor_session(monitor_session_id)
        if monitor_session:
            self.session.delete(monitor_session)
            self.session.commit()
            return True
        return False
