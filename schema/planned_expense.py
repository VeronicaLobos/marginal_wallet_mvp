"""
Planned Expense Schema

Planned expenses are future expenses that users
can plan for.

Users can create, update, delete and retrieve
planned expenses.

* One User can have multiple planned expenses.
"""

from __future__ import annotations
import enum
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class CurrencyType(str, enum.Enum):
    euro = "EURO"
    usd = "USD"

class FrequencyType(str, enum.Enum):
    weekly = "Weekly"
    monthly = "Monthly"
    quarterly = "Quarterly"
    biannually = "Biannually"
    yearly = "Yearly"
    one_time = "One Time"

class PlannedExpenseBase(SQLModel):
    date: Optional[datetime] = Field(nullable=True)
    value: float = Field(nullable=False)
    currency: CurrencyType = Field(nullable=False)
    frequency: FrequencyType = Field(nullable=False)

class PlannedExpenseCreate(PlannedExpenseBase):
    user_id: int

class PlannedExpenseUpdate(PlannedExpenseBase):
    date: Optional[datetime] = None
    value: Optional[float] = None
    currency: CurrencyType | None = None
    frequency: FrequencyType | None = None

class PlannedExpensePublic(PlannedExpenseBase):
    id: int
    user_id: int

class PlannedExpense(PlannedExpenseBase, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    user_id: int = Field(foreign_key="user.id")

    from schema.user import User
    user: "User" = Relationship(back_populates="planned_expenses")
