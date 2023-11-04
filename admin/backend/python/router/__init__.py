from fastapi import APIRouter

master_router = APIRouter(
    prefix='/api',
    tags=['master']
)

from .data import data_router
master_router.include_router(data_router)

