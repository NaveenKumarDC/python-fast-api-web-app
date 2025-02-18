from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str
    phone_number: str | None = None
    salary: Optional[float] = None