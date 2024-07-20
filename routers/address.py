import sys
sys.path.append('..')

from typing import Optional
from fastapi import APIRouter, Depends
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user

router = APIRouter(
  prefix="/address",
  tags=["address"],
  responses={404: {"description": "Not found"}}
)

def get_db():
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()

class Address(BaseModel):
  street: str
  city: str
  state: str
  zip: str
  country: str

