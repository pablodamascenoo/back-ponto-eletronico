from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    job: str
    workload: int
    tagId: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True