from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.db import session, models
from src.schemas import accounts as account_schemas
from src.api.endpoints.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[account_schemas.Account])
def read_accounts(db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    accounts = db.query(models.Account).filter(models.Account.user_id == current_user.id).all()
    # If no accounts, create default ones for demo
    if not accounts:
        default_accounts = [
            models.Account(user_id=current_user.id, name="Main Savings", balance=5234.50, type="Savings"),
            models.Account(user_id=current_user.id, name="Daily Checking", balance=1200.00, type="Checking"),
            models.Account(user_id=current_user.id, name="Credit Card", balance=-450.20, type="Credit")
        ]
        for acc in default_accounts:
            db.add(acc)
        db.commit()
        accounts = db.query(models.Account).filter(models.Account.user_id == current_user.id).all()
    return accounts

@router.post("/", response_model=account_schemas.Account)
def create_account(account: account_schemas.AccountCreate, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    db_account = models.Account(**account.model_dump(), user_id=current_user.id)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account
