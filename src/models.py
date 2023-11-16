from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class PIDSet(Base):
    __tablename__ = 'PID Sets'

    id = Column(Integer, primary_key=True)
    set_identifier = Column(String, unique=True, nullable=False)


class MonitorSession(Base):
    __tablename__ = 'Monitor Sessions'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False, default=datetime.now)
    end_time = Column(DateTime)
    set_id = Column(Integer, ForeignKey('pidset.id'), nullable=False)
    pid_set = relationship('PIDSet', back_populates='monitor_sessions')


class MonitorRecord(Base):
    __tablename__ = 'Monitor Records'

    id = Column(Integer, primary_key=True)
    time_stamp = Column(DateTime, nullable=False, default=datetime.now)
    status_code = Column(String, nullable=False)
    redirect_count = Column(Integer, nullable=False)
    monitoring_session_id = Column(Integer,
                                   ForeignKey('monitorsession.id'),
                                   nullable=False)
    monitoring_session = relationship('MonitorSession',
                                      back_populates='monitor_records')
