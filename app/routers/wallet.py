from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", response_model=list[schemas.User], tags=["Users"])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.put("/users/{user_id}/wallet", response_model=schemas.User, tags=["Wallet"])
def update_wallet(user_id: int, amount: float, type_: str, db: Session = Depends(get_db)):
    user = crud.update_wallet(db, user_id, amount, type_)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/{user_id}/transactions", response_model=list[schemas.Transaction], tags=["Transactions"])
def fetch_transactions(user_id: int, db: Session = Depends(get_db)):
    return crud.get_transactions(db, user_id)
