from datetime import datetime
from sqlalchemy.orm import Session

from database import get_db
from models import MonitorRecord


class MonitorRecordRepository:
    """
    Initialize the MonitorRecordRepository.

    This class provides CRUD operations for the MonitorRecord model.
    """
    def __init__(self) -> None:
        self.session: Session = get_db().__next__()

    def create_monitor_record(self, time_stamp: datetime, status_code: int,
                              redirect_count: int,
                              monitoring_session_id: int) -> MonitorRecord:
        monitor_record = MonitorRecord(
            time_stamp=time_stamp,
            status_code=status_code,
            redirect_count=redirect_count,
            monitoring_session_id=monitoring_session_id
        )
        self.session.add(monitor_record)
        self.session.commit()
        self.session.refresh(monitor_record)
        return monitor_record

    def get_monitor_record(self, monitor_record_id: int) -> MonitorRecord:
        return self.session.query(MonitorRecord).filter(
            MonitorRecord.id == monitor_record_id).first()

    def get_all_monitor_records(self) -> list[MonitorRecord]:
        return self.session.query(MonitorRecord).all()

    def get_monitor_records_for_session(self, monitoring_session_id: int
                                        ) -> list[MonitorRecord]:
        return self.session.query(MonitorRecord).filter(
            MonitorRecord.monitoring_session_id == monitoring_session_id).all()

    def delete_monitor_record(self, monitor_record_id: int) -> bool:
        monitor_record = self.get_monitor_record(monitor_record_id)
        if monitor_record:
            self.session.delete(monitor_record)
            self.session.commit()
            return True
        return False
