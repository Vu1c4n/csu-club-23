from fastapi import APIRouter
from gen_tb import *
from fastapi.responses import FileResponse
from cfg import DATA_PATH,CLUB_MAP
from z_file import zip_file

data_router = APIRouter(
    prefix='/data',
    tags = ['data']
)

@data_router.get('/table-one')
async def table_one(c_name:str):
    # 生成.xlsx文件
    print(c_name)
    gen_tb_one(c_name)
    f_path = DATA_PATH + 'output/' + c_name + '.xlsx'
    f_name = c_name + '.xlsx'
    rtn_file = FileResponse(
        path=f_path,
        filename = f_name
    )
    return rtn_file

@data_router.get('/table-all')
async def table_all():
    gen_tb_all(CLUB_MAP)
    zip_file()
    f_path = DATA_PATH + 'output/' + 'tables.zip'
    f_name = 'tables.zip'
    rtn_file = FileResponse(
        path=f_path,
        filename=f_name
    )
    return rtn_file
