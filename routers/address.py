import sys
sys.path.append('..')

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
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

@router.post("/")
def create_address(address: Address, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
  if user is None:
    raise HTTPException(status_code=401, detail="Authentication Failed")
  address_model = models.Address()

  address_model.street = address.street
  address_model.city = address.city
  address_model.state = address.state
  address_model.zip = address.zip
  address_model.country = address.country

  db.add(address_model)
  db.flush()
  
  user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
  user_model.address_id = address_model.id

  db.add(user_model)
  db.commit()
