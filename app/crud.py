from sqlalchemy.orm import Session
from . import models

def get_users(db: Session):
    return db.query(models.User).all()

def update_wallet(db: Session, user_id: int, amount: float, type_: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    user.wallet_balance += amount
    db.commit()
    db.refresh(user)
    # Create transaction record
    transaction = models.Transaction(
        user_id=user.id,
        amount=amount,
        type=type_
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return user

def get_transactions(db: Session, user_id: int):
    return db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()
