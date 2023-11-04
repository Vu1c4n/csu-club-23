from pydantic import BaseModel


class stu(BaseModel):
    name: str
    sex: str
    nation: str
    birth: str#时间选择
    political: str#picker
    stu_id: str#填东西算了
    stu_type: str  # 培养层次：本科生，研究生之类的
    specialty: str  # 专业
    grade: str
    academy: str
    stu_class: str
    from_location: str  # 生源地 海外 大陆 港澳台
    phone: str
    qq: str
