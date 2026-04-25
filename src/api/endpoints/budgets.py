from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db import models, session
from src.schemas import budgets as budget_schemas
from src.api.endpoints.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=list[budget_schemas.BudgetOut])
def list_budgets(
    db: Session = Depends(session.get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.Budget).filter(models.Budget.user_id == current_user.id).all()

@router.post("/", response_model=budget_schemas.BudgetOut)
def create_budget(
    budget: budget_schemas.BudgetCreate,
    db: Session = Depends(session.get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Check if budget already exists for this category/month
    existing = db.query(models.Budget).filter(
        models.Budget.user_id == current_user.id,
        models.Budget.category == budget.category,
        models.Budget.month == budget.month
    ).first()
    
    if existing:
        existing.limit_amount = budget.limit_amount
        db.commit()
        db.refresh(existing)
        return existing
        
    db_budget = models.Budget(**budget.dict(), user_id=current_user.id)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget
