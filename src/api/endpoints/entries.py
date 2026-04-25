from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db import models, session
from src.schemas import entries as entry_schemas
from src.api.endpoints.auth import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=entry_schemas.EntryOut)
def create_entry(
    entry: entry_schemas.EntryCreate, 
    db: Session = Depends(session.get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_entry = models.FinancialEntry(**entry.dict(), user_id=current_user.id)
    db.add(db_entry)
    
    # Update account balance if account_id is provided
    if entry.account_id:
        account = db.query(models.Account).filter(models.Account.id == entry.account_id).first()
        if account:
            if entry.type.lower() == "income":
                account.balance += entry.amount
            else:
                account.balance -= entry.amount
                
    # Update budget if it's an expense
    if entry.type.lower() == "expense" and entry.category:
        current_month = datetime.utcnow().strftime("%Y-%m")
        budget = db.query(models.Budget).filter(
            models.Budget.user_id == current_user.id,
            models.Budget.category == entry.category,
            models.Budget.month == current_month
        ).first()
        if budget:
            budget.spent_amount += entry.amount
    
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.get("/", response_model=list[entry_schemas.EntryOut])
def list_entries(
    db: Session = Depends(session.get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.FinancialEntry).filter(models.FinancialEntry.user_id == current_user.id).all()
