from fastapi import APIRouter, Header
from pydantic import BaseModel
import requests
from typing import Optional
import json
from model.stu_model import stu
import db
from utils import *
from cfg import *

stu_route = APIRouter(
    prefix="/stu",
    tags=["stu"]
)
# appid = 'wx2fdfc27744ffa252'
# secret = '9da819bd0531b325f5ebda4f85a92503'

appid = wx_app_cfg['appid']
secret = wx_app_cfg['secret']

def login(g):
    print("login使用的code:"+ " " + g)
    tokenInfo = json.loads(
        requests.get(
            url='https://api.weixin.qq.com/sns/oauth2/access_token',
            params={
                'appid': appid,
                'secret': secret,
                'code': g,
                'grant_type': 'authorization_code'
            }
        ).content.decode(), strict=False)
    print("tokenInfo below:>>>")
    print(tokenInfo)    
    if 'errcode' in tokenInfo:
        return falseReturn(msg=str(tokenInfo["errcode"]) + ' ' + tokenInfo["errmsg"])

    openID = tokenInfo['openid']
    access_token = tokenInfo['access_token']
    user_info = json.loads(
        requests.get(
            url='https://api.weixin.qq.com/sns/userinfo',
            params={
                'access_token': access_token,
                'openid': openID,
                'lang': 'zh_CN'
            }
        ).content.decode())
    if 'errcode' in user_info:
        return falseReturn(msg='网络请求出错')

    else:
        avatar = user_info['headimgurl']
        nickname = user_info['nickname']
        return trueReturn(data={
            'openid': openID,
            'nickname': nickname,
            'avatar': avatar
        })


class wxUser(BaseModel):
    code: str


@stu_route.post('/signin')
async def signin(f: wxUser):
    """微信鉴权的操作，对于每个微信用户是一个单独的user"""
    print("传过来的code:..."+ f.code)
    m = login(f.code)  # 获取openid
    print(m)
    if (m['data'] != None):  # 判断是否获得到了信息
        x = m['data']
        if (db.stu.find_one({"openid": x['openid']}) == None):  # 判断该微信用户是否为第一次
            x['name'] = ""
            x['sex'] = ""
            x['nation'] = ""
            x['birth'] = ""
            x['political'] = ""
            x['stu_id'] = ""
            x['stu_type'] = ""
            x['specialty'] = ""
            x['grade'] = ""
            x['academy'] = ""
            x['stu_class'] = ""
            x['from_location'] = ""
            x['phone'] = ""
            x['qq'] = ""
            x['_id'] = x['openid']
            db.stu_insert_one(x)
            return trueReturn(data={"token": x['_id'], "picture": x['avatar']})
        else:
            token = db.stu.find_one({"openid": x['openid']})['_id']
            return trueReturn(data={"token": token, "picture": x['avatar']})


@stu_route.post('/stu_msg')
async def stu_msg(f: stu, token: str):
    """进入后先填写信息"""

    data = {
        "name": f.name,
        "sex": f.sex,
        "nation": f.nation,
        "birth": f.birth,
        "political": f.political,
        "stu_id": f.stu_id,
        "stu_type": f.stu_type,
        "specialty": f.specialty,
        "grade": f.grade,
        "academy": f.academy,
        "stu_class": f.stu_class,
        "from_location": f.from_location,
        "phone": f.phone,
        "qq": f.qq
    }
    db.stu_updata_one(token, data)
    return trueReturn(msg="信息填入成功")


@stu_route.get('/get_msg')
async def get_msg(token: str):
    """通过token值获取这个人的全部信息"""
    print(token)
    x = db.stu_find_one(token)
    print(x)
    del x['_id']
    del x['openid']
    return trueReturn(data=x)
