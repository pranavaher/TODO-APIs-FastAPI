from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

class CreateUserRequest(BaseModel):
  email = str
  username = str
  first_name = str
  last_name = str
  password = str
  role = str

@router.get("/auth/")
async def get_user():
  return { "message": "authenticated" }
