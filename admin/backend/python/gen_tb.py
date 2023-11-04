import openpyxl
from dao import *
from model import *
from w_excel import write
from model import Club

# private member
# __club_list = club_all()

def __stu_list(token_list):
    rtn_list = list()
    for token in token_list:
        stu = stu_info(token)
        rtn_list.append(stu)
    return rtn_list


# APIs
def gen_tb_one(c_name:str):
    print('Generating: '+c_name+'.xlsx')
    club = club_one(c_name)
    # raw data
    index = club['_id']
    token_list = club['applicant']

    # gen data
    stu_list = __stu_list(token_list)
    name = club_name(index)

    # 写表
    write(name,stu_list)

def gen_tb_all(club_list:list):
    for club in club_list:
        gen_tb_one(club)

# unit_test
if __name__ == '__main__':
    # club:Club = club_one()
    gen_tb_all(CLUB_MAP)