from pydantic import BaseModel
from typing import List
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    phone: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    wallet_balance: float

    class Config:
        from_attributes = True

class Transaction(BaseModel):
    id: int
    user_id: int
    amount: float
    type: str
    timestamp: datetime

    class Config:
        from_attributes = True
    