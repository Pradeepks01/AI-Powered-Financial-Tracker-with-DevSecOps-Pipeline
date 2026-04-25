from pydantic import BaseModel
from typing import Optional

class BudgetBase(BaseModel):
    category: str
    limit_amount: float
    month: str  # YYYY-MM

class BudgetCreate(BudgetBase):
    pass

class BudgetOut(BudgetBase):
    id: int
    spent_amount: float

    class Config:
        from_attributes = True
