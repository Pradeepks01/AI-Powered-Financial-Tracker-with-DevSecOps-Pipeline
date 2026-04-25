from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EntryBase(BaseModel):
    amount: float
    type: str
    category: str
    description: Optional[str] = None
    account_id: Optional[int] = None

class EntryCreate(EntryBase):
    pass

class EntryOut(EntryBase):
    id: int
    timestamp: datetime
    account_id: Optional[int] = None

    class Config:
        from_attributes = True
