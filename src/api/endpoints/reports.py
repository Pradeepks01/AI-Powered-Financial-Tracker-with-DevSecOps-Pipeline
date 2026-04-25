from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.db import models, session
from src.api.endpoints.auth import get_current_user
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/summary")
def get_summary(
    db: Session = Depends(session.get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Income vs Expense summary for last 30 days
    last_30_days = datetime.utcnow() - timedelta(days=30)
    
    stats = db.query(
        models.FinancialEntry.type,
        func.sum(models.FinancialEntry.amount).label("total")
    ).filter(
        models.FinancialEntry.user_id == current_user.id,
        models.FinancialEntry.timestamp >= last_30_days
    ).group_by(models.FinancialEntry.type).all()
    
    # Category breakdown
    categories = db.query(
        models.FinancialEntry.category,
        func.sum(models.FinancialEntry.amount).label("total")
    ).filter(
        models.FinancialEntry.user_id == current_user.id,
        models.FinancialEntry.type == "expense"
    ).group_by(models.FinancialEntry.category).all()
    
    return {
        "stats": {s.type: s.total for s in stats},
        "categories": {c.category: c.total for c in categories}
    }
