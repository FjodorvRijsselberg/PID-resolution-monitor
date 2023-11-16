from fastapi import FastAPI

from api import router


def create_server(repositories):
    server = FastAPI()
    server.include_router(router)
    server.repositories = repositories
    return server
