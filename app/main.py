from fastapi import FastAPI
from .routers import wallet
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Wallet Assignment API")
app.include_router(wallet.router)

# Run with: uvicorn app.main:app --reload
