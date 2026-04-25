from pydantic import BaseModel
from typing import Optional

class AccountBase(BaseModel):
    name: str
    type: str
    balance: float = 0.0

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
