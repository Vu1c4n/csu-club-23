from pydantic import BaseModel


class apply(BaseModel):
    index:str
    obname: str  # 社团名称
