from fastapi import APIRouter
import db
from model.apply_model import apply
from utils import *

apply_route = APIRouter(
    prefix="/apply",
    tags=["apply"]
)

UPPER_BOUND:int = 2 # 每个人报名社团上限


@apply_route.post('/send_msg')
async def send_msg(f: apply, token: str):
    """报名：将token和部门进行绑定"""
    try:
        all_apply = []
        for x in db.apply_get_apply(token):
            all_apply.append(x['index'])
        if (f.index in all_apply):
            return falseReturn(msg="已经报名此社团")
        elif(len(all_apply) >= UPPER_BOUND):
            msg ="最多同时报名"+ str(UPPER_BOUND) + "个社团"
            return falseReturn(msg=msg)
        else:
            db.apply_insert_one(dict(f), token)
            db.club_insert_one(f.index, token)
            db.export_insert_one(f.index,token) # export部分
            return trueReturn()
    except Exception as e:
        return falseReturn(msg=str(e))


@apply_route.get('/get_apply')
async def get_apply(token: str):
    """通过token获取一个成员报名的全部数据"""
    return trueReturn(data=db.apply_get_apply(token))


@apply_route.get('/get_pratical')
async def get_apply(token: str):
    """通过token获取一个成员报名的全部部门的index和name"""
    all = []
    x = db.apply_get_apply(token)
    for i in x:
        all.append({"index": i['index'], "obname": i['obname']})
    return trueReturn(all)


@apply_route.post('/del_apply')
async def del_apply(index: str, token: str):
    """通过index和token删除一次报名"""
    db.apply_del_one(index, token)
    db.club_del_one(index, token)
    try:
        db.export_del_one(index,token) # export部分
    except:
        print("sth go wrong when deleting index:"+index)
    return trueReturn()

@apply_route.get('/options')
async def options():
    op=db.static_options()
    return trueReturn(data=op)
