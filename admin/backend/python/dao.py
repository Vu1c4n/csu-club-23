# db.py 封装数据库相关操作

import pymongo
from cfg import *
from model import Club

# private member
__OMIT_RULE = {'_id':0,'openid':0,'nickname':0,'avatar':0,'apply':0}
__clt = pymongo.MongoClient(**database_cfg)
__db = __clt['club23']

__export = __db['export']
__stu = __db['stu']


def __club_index(name:str):
    return CLUB_MAP.index(name)

# APIs
def club_name(index:int):
    return CLUB_MAP[index]

def club_all():
    rtn_list:list = __export.find() # 获取整体club报名情况列表
    return rtn_list

def club_one(name:str) -> Club : 
    index = __club_index(name)
    rtn:Club = __export.find_one({'_id':index})
    return rtn

def stu_info(token:str):
    s = __stu.find_one({'_id':token},__OMIT_RULE)
    return s

# unit_test
# if __name__ == '__main__':
#     __STU_LIST = __stu_list()
#     print(stu_info('o0EOcsz_RZn5Gry3EBPThwmF5YVE'))
#     # print(club_name(0))
