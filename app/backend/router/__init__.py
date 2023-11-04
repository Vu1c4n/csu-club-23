from fastapi import APIRouter, Depends

master_router = APIRouter(
    prefix="/api",
    tags=["master"]
)

from .stu import stu_route
from .apply import apply_route
from .club import club_route
master_router.include_router(stu_route)
master_router.include_router(club_route)
master_router.include_router(apply_route)