import models
from database import engine
from repositories.record_repository import MonitorRecordRepository
from repositories.session_repository import MonitorSessionRepository
from repositories.set_repository import PIDSetRepository
from server import create_server

pid_set_repository = PIDSetRepository()
monitor_session_repository = MonitorSessionRepository()
monitor_record_repository = MonitorRecordRepository()
repositories = {
    "pid_set_repository": pid_set_repository,
    "monitor_session_repository": monitor_session_repository,
    "monitor_record_repository": monitor_record_repository,
}

models.Base.metadata.create_all(bind=engine)

server = create_server(repositories=repositories)
