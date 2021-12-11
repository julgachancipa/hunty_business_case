from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Company(BaseModel):
    id: Optional[int]
    name: Optional[str]
    link: Optional[str]
    country: Optional[str]
    city: Optional[str]
    date_added: Optional[datetime]
    contact_first_name: Optional[str]
    contact_last_name: Optional[str]
    contact_phone_number: Optional[str]
    contact_email: Optional[str]
