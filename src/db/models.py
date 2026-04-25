from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(255))
    entries = relationship("FinancialEntry", back_populates="user")
    accounts = relationship("Account", back_populates="user")
    budgets = relationship("Budget", back_populates="user")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    balance = Column(Float, default=0.0)
    type = Column(String(50))  # Savings, Credit Card, etc.
    user = relationship("User", back_populates="accounts")
    entries = relationship("FinancialEntry", back_populates="account")

class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String(50))
    limit_amount = Column(Float)
    spent_amount = Column(Float, default=0.0)
    month = Column(String(7))  # YYYY-MM
    user = relationship("User", back_populates="budgets")

class FinancialEntry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)
    amount = Column(Float)
    type = Column(String(20))  # Income or Expense
    category = Column(String(50))
    description = Column(String(255), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="entries")
    account = relationship("Account", back_populates="entries")
