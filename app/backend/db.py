import pymongo
from cfg import *

myclient = pymongo.MongoClient(**database_cfg)


# 介绍数据库架构
# 一个shetuan库（这个无所谓）
# 三个表stu(每个用户的信息),apply(注册信息),club(社团信息)
mydb = myclient['club23']
stu = mydb['stu']
apply = mydb['apply']
club = mydb['club']
all_club = mydb['all_club']
export = mydb['export']
static = mydb['static']

def stu_insert_one(a):
    stu.insert_one(a)

def stu_find_one(_id):
    res = stu.find_one({"_id": _id})
    return res

def stu_updata_one(id, msg):
    myquery = {"_id": id}
    newvalues = {"$set": msg}

    stu.update_one(myquery, newvalues)


def stu_update_apply(id, index):
    s = stu_find_one(id)
    apply:list = s['apply']
    print(apply)
    apply.append(index)
    new_values = {"$set":{'apply':apply}}
    stu.update_one({"_id":id}, new_values)

def apply_insert_one(data, token):
    x = data
    x['token'] = token
    apply.insert_one(x)

def apply_del_one(index, token):
    apply.delete_one({"index": index, "token": token})

def apply_get_apply(token):
    x = []
    for i in apply.find({"token": token}):
        del i['_id']
        x.append(i)
    return x

def club_insert_one(index, token):
    club.insert_one({
        "index": index,
        "token": token
    })

def club_del_one(index, token):
    club.delete_one({"index": index, "token": token})

def club_list_get_allclub():
    allclub = all_club.find_one({"_id": "allclub"})
    return allclub

def static_get_all_club():
    return static.find_one({'_id':'all_club'})

def static_options():    
    """选择专业的下拉列表"""
    op_23 = static.find_one({"_id":"options-23"})["data"]
    op_all =static.find_one({"_id":"options-all"})["data"]
    return [op_23, op_all]

def export_insert_one(index:str,token:str):
    index = int(index)
    club = export.find_one({'_id':index})
    applicant:list = club['applicant']
    applicant.append(token)
    export.update_one({'_id':index},{'$set':{'applicant':applicant}})

def export_del_one(index:str,token:str):
    index = int(index)
    club = export.find_one({'_id':index})
    applicant:list = club['applicant']
    applicant.remove(token)
    export.update_one({'_id':index},{'$set':{'applicant':applicant}})
