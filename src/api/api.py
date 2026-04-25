from fastapi import APIRouter
from src.api.endpoints import auth, entries, chat, accounts, budgets, reports

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(entries.router, prefix="/entries", tags=["entries"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(budgets.router, prefix="/budgets", tags=["budgets"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
