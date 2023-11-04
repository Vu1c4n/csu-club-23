from fastapi import APIRouter

import db

club_route = APIRouter(
    prefix="/club",
    tags=["club"]
)

from utils import *

@club_route.get('/allclub')
async def get_allclub():
    """获取全部的社团信息给前端用"""
    all_club = db.static_get_all_club()
    del all_club['_id']
    return all_club['data']
